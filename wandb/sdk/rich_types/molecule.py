import pathlib
from typing import Any, Dict, Optional, Sequence, TextIO, Union

from .media import Media, MediaSequence, register

# import rdkit.Chem


class Molecule(Media):
    OBJ_TYPE = "molecule-file"
    RELATIVE_PATH = pathlib.Path("media") / "molecule"

    SUPPORTED_TYPES = {
        "pdb",
        "pqr",
        "mmcif",
        "mcif",
        "cif",
        "sdf",
        "sd",
        "gro",
        "mol2",
        "mmtf",
    }

    SUPPORTED_RDKIT_TYPES = {"mol", "sdf"}

    _caption: Optional[str]

    def __init__(
        self,
        data_or_path,
        caption: Optional[str] = None,
        file_type: Optional[str] = None,
        **kwargs,
    ) -> None:
        super().__init__()
        self._caption = caption
        if isinstance(data_or_path, pathlib.Path):
            self.from_path(data_or_path)
        elif isinstance(data_or_path, str):
            self.from_string(data_or_path, file_type=file_type)
        elif hasattr(data_or_path, "read"):
            self.from_buffer(data_or_path, file_type)
        else:
            raise ValueError(f"Unsupported type: {type(data_or_path)}")

    def from_buffer(self, buffer: TextIO, file_type: Optional[str] = None) -> None:
        if file_type not in self.SUPPORTED_TYPES:
            raise ValueError(f"Unsupported file type: {file_type}")
        self._format = file_type
        with self.manager.save(suffix=f".{self._format}") as path:
            if hasattr(buffer, "seek"):
                buffer.seek(0)
            mol = buffer.read()
            with open(path, "w") as f:
                f.write(mol)

    def from_path(self, path: Union[str, pathlib.Path]) -> None:
        with self.manager.save(path) as path:
            self._format = path.suffix[1:].lower()
            assert (
                self._format in self.SUPPORTED_TYPES
            ), f"Unsupported file type: {self._format}"

    def from_string(self, data_or_path: str, file_type: Optional[str] = None) -> None:
        path = pathlib.Path(data_or_path)
        if path.suffix[:1] in self.SUPPORTED_TYPES:
            self.from_path(path)
        else:
            pass


@register(Molecule)
class MoleculeSequence(MediaSequence[Any, Molecule]):
    OBJ_TYPE = "molecule"
    OBJ_ARTIFACT_TYPE = "molecule"

    def __init__(self, items: Sequence[Any]):
        super().__init__(items, Molecule)

    def bind_to_artifact(self, artifact: "Artifact") -> Dict[str, Any]:
        super().bind_to_artifact(artifact)
        return {
            "_type": self.OBJ_ARTIFACT_TYPE,
        }

    def to_json(self) -> dict:
        items = [item.to_json() for item in self._items]
        return {
            "_type": self.OBJ_TYPE,
            "count": len(items),
            "filenames": [item["path"] for item in items],
            "captions": [item.caption for item in self._items],
        }

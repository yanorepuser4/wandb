"""Create informative charts for scikit-learn models and log them to W&B."""

from .plot import (
    plot_calibration_curve,
    plot_class_proportions,
    plot_classifier,
    plot_clusterer,
    plot_confusion_matrix,
    plot_elbow_curve,
    plot_feature_importances,
    plot_learning_curve,
    plot_outlier_candidates,
    plot_precision_recall,
    plot_regressor,
    plot_residuals,
    plot_roc,
    plot_silhouette,
    plot_summary_metrics,
)

__all__ = [
    "plot_classifier",
    "plot_clusterer",
    "plot_regressor",
    "plot_summary_metrics",
    "plot_learning_curve",
    "plot_feature_importances",
    "plot_class_proportions",
    "plot_calibration_curve",
    "plot_roc",
    "plot_precision_recall",
    "plot_confusion_matrix",
    "plot_elbow_curve",
    "plot_silhouette",
    "plot_residuals",
    "plot_outlier_candidates",
]

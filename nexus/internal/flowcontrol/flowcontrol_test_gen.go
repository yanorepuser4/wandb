// Code generated by MockGen. DO NOT EDIT.
// Source: flowcontrol_test.go

// Package flowcontrol is a generated GoMock package.
package flowcontrol

import (
	reflect "reflect"

	gomock "github.com/golang/mock/gomock"
	service "github.com/wandb/wandb/nexus/pkg/service"
)

// MockTestFlow is a mock of TestFlow interface.
type MockTestFlow struct {
	ctrl     *gomock.Controller
	recorder *MockTestFlowMockRecorder
}

// MockTestFlowMockRecorder is the mock recorder for MockTestFlow.
type MockTestFlowMockRecorder struct {
	mock *MockTestFlow
}

// NewMockTestFlow creates a new mock instance.
func NewMockTestFlow(ctrl *gomock.Controller) *MockTestFlow {
	mock := &MockTestFlow{ctrl: ctrl}
	mock.recorder = &MockTestFlowMockRecorder{mock}
	return mock
}

// EXPECT returns an object that allows the caller to indicate expected use.
func (m *MockTestFlow) EXPECT() *MockTestFlowMockRecorder {
	return m.recorder
}

// RecoverRecords mocks base method.
func (m *MockTestFlow) RecoverRecords(startOffset, endOffset int64) {
	m.ctrl.T.Helper()
	m.ctrl.Call(m, "RecoverRecords", startOffset, endOffset)
}

// RecoverRecords indicates an expected call of RecoverRecords.
func (mr *MockTestFlowMockRecorder) RecoverRecords(startOffset, endOffset interface{}) *gomock.Call {
	mr.mock.ctrl.T.Helper()
	return mr.mock.ctrl.RecordCallWithMethodType(mr.mock, "RecoverRecords", reflect.TypeOf((*MockTestFlow)(nil).RecoverRecords), startOffset, endOffset)
}

// SendPause mocks base method.
func (m *MockTestFlow) SendPause() {
	m.ctrl.T.Helper()
	m.ctrl.Call(m, "SendPause")
}

// SendPause indicates an expected call of SendPause.
func (mr *MockTestFlowMockRecorder) SendPause() *gomock.Call {
	mr.mock.ctrl.T.Helper()
	return mr.mock.ctrl.RecordCallWithMethodType(mr.mock, "SendPause", reflect.TypeOf((*MockTestFlow)(nil).SendPause))
}

// SendRecord mocks base method.
func (m *MockTestFlow) SendRecord(record *service.Record) {
	m.ctrl.T.Helper()
	m.ctrl.Call(m, "SendRecord", record)
}

// SendRecord indicates an expected call of SendRecord.
func (mr *MockTestFlowMockRecorder) SendRecord(record interface{}) *gomock.Call {
	mr.mock.ctrl.T.Helper()
	return mr.mock.ctrl.RecordCallWithMethodType(mr.mock, "SendRecord", reflect.TypeOf((*MockTestFlow)(nil).SendRecord), record)
}

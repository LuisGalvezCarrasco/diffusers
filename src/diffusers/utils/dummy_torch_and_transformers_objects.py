# This file is autogenerated by the command `make fix-copies`, do not edit.
# flake8: noqa

from ..utils import DummyObject, requires_backends


class LDMTextToImagePipeline(metaclass=DummyObject):
    _backends = ["torch", "transformers"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["torch", "transformers"])

    @classmethod
    def from_config(cls, *args, **kwargs):
        requires_backends(cls, ["torch", "transformers"])

    @classmethod
    def from_pretrained(cls, *args, **kwargs):
        requires_backends(cls, ["torch", "transformers"])


class StableDiffusionImg2ImgPipeline(metaclass=DummyObject):
    _backends = ["torch", "transformers"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["torch", "transformers"])

    @classmethod
    def from_config(cls, *args, **kwargs):
        requires_backends(cls, ["torch", "transformers"])

    @classmethod
    def from_pretrained(cls, *args, **kwargs):
        requires_backends(cls, ["torch", "transformers"])


class StableDiffusionInpaintPipeline(metaclass=DummyObject):
    _backends = ["torch", "transformers"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["torch", "transformers"])

    @classmethod
    def from_config(cls, *args, **kwargs):
        requires_backends(cls, ["torch", "transformers"])

    @classmethod
    def from_pretrained(cls, *args, **kwargs):
        requires_backends(cls, ["torch", "transformers"])


class StableDiffusionPipeline(metaclass=DummyObject):
    _backends = ["torch", "transformers"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["torch", "transformers"])

    @classmethod
    def from_config(cls, *args, **kwargs):
        requires_backends(cls, ["torch", "transformers"])

    @classmethod
    def from_pretrained(cls, *args, **kwargs):
        requires_backends(cls, ["torch", "transformers"])

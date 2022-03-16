import pytest
from model import SynthesizabilityModel

@pytest.fixture()
def model():
    model = SynthesizabilityModel()
    return model

@pytest.mark.parametrize(
    "material",
    [
        1234,
        dict({"a":"b"}),
        ["Fe2O3"],
        ["Fe2", "O3"],
    ]
)
def test_invalid_material(material:str, model:SynthesizabilityModel) -> None:
    with pytest.raises(TypeError):
        model.predict_single(material)

@pytest.mark.parametrize(
    "material",
    [
        "Li7La3(SnO6)2",
        "Li3(WO3)8",
        "Li4Mn2P4H3O16",
        "Li2Ni(PO3)5",
        "MgV2O4",
    ]
)
def test_prediction_bounds(material:str, model:SynthesizabilityModel) -> None:
    predicted_value = model.predict_single(material)
    assert 0 <= predicted_value <= 1

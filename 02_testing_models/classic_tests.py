import pytest
from model import SynthesizabilityModel

@pytest.fixture()
def synthesizability_model():
    model = SynthesizabilityModel()
    return model

@pytest.mark.parametrize(
    "input_val",
    [
        "Li7La3(SnO6)2",
        "Li3(WO3)8",
        "Li4Mn2P4H3O16",
        "Li2Ni(PO3)5",
        "MgV2O4",
    ]
)
def test_prediction_bounds(input_val:str) -> None:
    predicted_value = synthesizability_model.predict_single(input_val)
    assert 0 <= predicted_value <= 1
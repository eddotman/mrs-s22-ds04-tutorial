import pytest
from model import SynthesizabilityModel

@pytest.fixture()
def synthesizability_model():
    model = SynthesizabilityModel()
    return model

@pytest.mark.parametrize(
    "input_val",
    [
        [
            "MgV2O4",
            "MgV8O4",
            "MgV24O4",
        ],
        [
            "Li3(WO3)8",
            "Li3(W5O3)8",
            "Li3(W20O3)8",
        ]
    ]
)
def test_stoichiometric_monotonicity(input_series:str) -> None:
    predicted_values = [
        synthesizability_model.predict_single(input_val)
        for input_val in input_series
    ]

    assert predicted_values == sorted(predicted_values, reverse=True)
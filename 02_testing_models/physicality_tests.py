import pytest
from model import SynthesizabilityModel

@pytest.fixture()
def synthesizability_model():
    model = SynthesizabilityModel()
    return model

@pytest.mark.parametrize(
    "input_series",
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
@pytest.mark.xfail(reason="Too hard for a random model!")
def test_stoichiometric_monotonicity(input_series:str) -> None:
    predicted_values = [
        synthesizability_model.predict_single(input_val)
        for input_val in input_series
    ]

    assert predicted_values == sorted(predicted_values, reverse=True)

@pytest.mark.parametrize(
    "input_series",
    [
        [
            "MgV2O4",
            "O4MgV2",
            "V2MgO4",
        ],
        [
            "Li3(WO3)8",
            "(WO3)8Li3",
        ]
    ]
)
@pytest.mark.xfail(reason="Too hard for a random model!")
def test_atomic_order(input_series:str) -> None:
    predicted_values = [
        synthesizability_model.predict_single(input_val)
        for input_val in input_series
    ]

    assert max(predicted_values) - min(predicted_values) < 0.001
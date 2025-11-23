import pandas as pd


def test_load_sample():
df = pd.DataFrame({"a":[1,2,3]})
assert df.shape[0] == 3
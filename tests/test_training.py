from predict_pv_yield.training import train
import os

from hydra import compose, initialize


def test_train():

    os.environ["NEPTUNE_API_TOKEN"] = "not_a_token"

    initialize(config_path="../configs", job_name="test_app")
    config = compose(
        config_name="config",
        overrides=["logger=csv", "experiment=example_simple", "datamodule.fake_data=true", "trainer.fast_dev_run=true"],
    )

    train(config=config)

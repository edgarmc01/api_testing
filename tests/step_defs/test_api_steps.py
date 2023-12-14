import os 
from pytest_bdd import scenarios
from main.core.utils.logger import logger_request
from tests.step_defs.common_action_steps import *
from tests.step_defs.common_action_steps import *

logger_request.info("execition the selected features")
feature_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "features"
)
scenarios(feature_path)
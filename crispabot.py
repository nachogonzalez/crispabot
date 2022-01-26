import json
import xlsxwriter
from loguru import logger
from utils import loadCongressmen
from utils import getNames
from utils import getGroups
from utils import loadExcel

logger.info("Starting CrispaBot")

loadExcel()
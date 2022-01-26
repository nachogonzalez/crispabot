import json
import xlsxwriter
from loguru import logger

# Read the congressmen file function
def loadCongressmen(jsonfile):
	# We use the “utf-8” encoding to map byte values directly to the first 256 Unicode code points
	with open("data/DiputadosActivos.json", encoding='utf-8') as f:
		data = json.load(f)
	f.close()
	return data
	
def getNames(data):
	namesList = []
	i = 0
	for item in data:
		element = data[i]
		namesList.append(element["NOMBRE"])
		i = i + 1
	return namesList
	
def getGroups(data):
	groupsList = []
	i = 0
	for item in data:
		element = data[i]
		groupsList.append(element["GRUPOPARLAMENTARIO"])
		i = i + 1
	return groupsList
	
# Auxiliar function to load the data from the JSON file into an excel, that will be completed with the twitter accounts.
def loadExcel():
	data = loadCongressmen("data/DiputadosActivos")
	namesList = getNames(data)
	groupsList = getGroups(data)
	workbook = xlsxwriter.Workbook('data/diputados.xlsx')
	worksheet = workbook.add_worksheet()
	i = 0
	contador_celda = 0
	for item in data:
		nombre = str(namesList[i])
		grupo = groupsList[i]
		logger.debug("Diputado número: " + str(i))
		logger.debug("Nombre: " + nombre)
		logger.debug("Grupo: " + grupo)
		contador_celda = contador_celda + 1
		celdaNombre = "A" + str(contador_celda)
		celdaGrupo = "B" + str(contador_celda)
		worksheet.write(celdaNombre, nombre)
		worksheet.write(celdaGrupo, grupo)
		i = i + 1
	workbook.close()
	return()
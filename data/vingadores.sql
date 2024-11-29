-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: vingadores
-- ------------------------------------------------------
-- Server version	8.0.35

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `heroi`
--

DROP TABLE IF EXISTS `heroi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `heroi` (
  `idheroi` int NOT NULL AUTO_INCREMENT,
  `nome_heroi` varchar(45) DEFAULT NULL,
  `nome_real` varchar(45) DEFAULT NULL,
  `categoria` varchar(45) DEFAULT NULL,
  `poderes` varchar(45) DEFAULT NULL,
  `poder_principal` varchar(45) DEFAULT NULL,
  `fraquezas` varchar(45) DEFAULT NULL,
  `nivel_forca` int DEFAULT NULL,
  PRIMARY KEY (`idheroi`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Heroi cadastrados no sistema.';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `heroi`
--

LOCK TABLES `heroi` WRITE;
/*!40000 ALTER TABLE `heroi` DISABLE KEYS */;
INSERT INTO `heroi` VALUES (1,'Homem de Ferro','Tony Stark','Humano','Armadura, voar','Armadura','Impostos',100),(2,'Capitão América','Steve Rogers','Humano','Escudo,  força','Escudo','Gelo,  Hidra',350);
/*!40000 ALTER TABLE `heroi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `heroi_localizador`
--

DROP TABLE IF EXISTS `heroi_localizador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `heroi_localizador` (
  `idheroi_localizador` int NOT NULL AUTO_INCREMENT,
  `idheroi` int NOT NULL,
  `idlocalizador` int NOT NULL,
  PRIMARY KEY (`idheroi_localizador`),
  KEY `idheroi_idx` (`idheroi`),
  KEY `idlocalizador_idx` (`idlocalizador`),
  CONSTRAINT `id_heroi` FOREIGN KEY (`idheroi`) REFERENCES `heroi` (`idheroi`),
  CONSTRAINT `id_localizador` FOREIGN KEY (`idlocalizador`) REFERENCES `localizador` (`idlocalizador`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `heroi_localizador`
--

LOCK TABLES `heroi_localizador` WRITE;
/*!40000 ALTER TABLE `heroi_localizador` DISABLE KEYS */;
/*!40000 ALTER TABLE `heroi_localizador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `heroi_tornozeleira`
--

DROP TABLE IF EXISTS `heroi_tornozeleira`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `heroi_tornozeleira` (
  `idheroi_tornozeleira` int NOT NULL AUTO_INCREMENT,
  `idheroi` int NOT NULL,
  `idtornozeleira` int NOT NULL,
  PRIMARY KEY (`idheroi_tornozeleira`),
  KEY `idheroi_idx` (`idheroi`),
  KEY `idtornozeleira_idx` (`idtornozeleira`),
  CONSTRAINT `idheroi` FOREIGN KEY (`idheroi`) REFERENCES `heroi` (`idheroi`),
  CONSTRAINT `idtornozeleira` FOREIGN KEY (`idtornozeleira`) REFERENCES `tornozeleira` (`idtornozeleira`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `heroi_tornozeleira`
--

LOCK TABLES `heroi_tornozeleira` WRITE;
/*!40000 ALTER TABLE `heroi_tornozeleira` DISABLE KEYS */;
/*!40000 ALTER TABLE `heroi_tornozeleira` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `localizador`
--

DROP TABLE IF EXISTS `localizador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `localizador` (
  `idlocalizador` int NOT NULL AUTO_INCREMENT,
  `localizacao_atual` varchar(50) NOT NULL,
  `ultima_localizacao` varchar(50) NOT NULL,
  `data_desativacao` datetime DEFAULT NULL,
  PRIMARY KEY (`idlocalizador`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `localizador`
--

LOCK TABLES `localizador` WRITE;
/*!40000 ALTER TABLE `localizador` DISABLE KEYS */;
/*!40000 ALTER TABLE `localizador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tornozeleira`
--

DROP TABLE IF EXISTS `tornozeleira`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tornozeleira` (
  `idtornozeleira` int NOT NULL AUTO_INCREMENT,
  `status` varchar(10) NOT NULL DEFAULT 'N/A',
  `data_ativacao` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `data_desativacao` datetime DEFAULT NULL,
  PRIMARY KEY (`idtornozeleira`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tornozeleira`
--

LOCK TABLES `tornozeleira` WRITE;
/*!40000 ALTER TABLE `tornozeleira` DISABLE KEYS */;
/*!40000 ALTER TABLE `tornozeleira` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'vingadores'
--

--
-- Dumping routines for database 'vingadores'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-27 16:29:47

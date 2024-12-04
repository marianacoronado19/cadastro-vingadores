CREATE DATABASE  IF NOT EXISTS `vingadores` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `vingadores`;
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
-- Table structure for table `convocacao`
--

DROP TABLE IF EXISTS `convocacao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `convocacao` (
  `idconvocacao` int NOT NULL AUTO_INCREMENT,
  `motivo` varchar(255) NOT NULL,
  `data_convocacao` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `data_comparecimento` datetime DEFAULT NULL,
  `status_convocacao` enum('Pendente','Ausente','Comparecido') NOT NULL DEFAULT 'Pendente',
  PRIMARY KEY (`idconvocacao`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `convocacao`
--

LOCK TABLES `convocacao` WRITE;
/*!40000 ALTER TABLE `convocacao` DISABLE KEYS */;
INSERT INTO `convocacao` VALUES (1,'O herói voou acima do limite permito pela S.H.I.E.L.D.','2019-05-07 14:58:00','2020-05-06 23:59:00','Comparecido'),(2,'O herói exterminou uma cidade inteira durante um período de descontrole (10 minutos).','2024-02-10 12:46:00','2024-02-12 19:22:00','Comparecido'),(3,'O herói acidentalmente derrubou seu martelo, \'Mjölnir\', na cabeça de um civil. O civil infelizmente faleceu.','2024-11-29 14:28:25',NULL,'Pendente'),(4,'O herói \"acidentalmente\" derrubou uma caixa d\'água enquanto se pendurava com suas teias.','2023-12-25 00:00:00','2024-04-14 03:45:00','Comparecido');
/*!40000 ALTER TABLE `convocacao` ENABLE KEYS */;
UNLOCK TABLES;

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
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Heroi cadastrados no sistema.';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `heroi`
--

LOCK TABLES `heroi` WRITE;
/*!40000 ALTER TABLE `heroi` DISABLE KEYS */;
INSERT INTO `heroi` VALUES (1,'Homem de Ferro','Tony Stark','Humano','Armadura, voar','Armadura','Impostos',100),(2,'Capitão América','Steve Rogers','Humano','Escudo,  força','Escudo','Gelo,  Hidra',350),(3,'Thor','Thor Odinson','Deidade','Martelo,  Raio,  Voar','Raios','Loki',5000),(4,'Hulk','Bruce Banner','Meta-Humano','Força','Força','Inteligência',1000),(5,'Homem Aranha','Peter Parker','Meta-Humano','Teia,  sentido aranha','Teia','Mary Jane',650);
/*!40000 ALTER TABLE `heroi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `heroi_convocacao`
--

DROP TABLE IF EXISTS `heroi_convocacao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `heroi_convocacao` (
  `idheroi_convocacao` int NOT NULL AUTO_INCREMENT,
  `idheroi` int NOT NULL,
  `idconvocacao` int NOT NULL,
  PRIMARY KEY (`idheroi_convocacao`),
  KEY `fk_heroiconvocacao_heroi_idx` (`idheroi`),
  KEY `fk_heroiconvocacao_convocacao_idx` (`idconvocacao`),
  CONSTRAINT `fk_heroiconvocacao_convocacao` FOREIGN KEY (`idconvocacao`) REFERENCES `convocacao` (`idconvocacao`),
  CONSTRAINT `fk_heroiconvocacao_heroi` FOREIGN KEY (`idheroi`) REFERENCES `heroi` (`idheroi`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `heroi_convocacao`
--

LOCK TABLES `heroi_convocacao` WRITE;
/*!40000 ALTER TABLE `heroi_convocacao` DISABLE KEYS */;
INSERT INTO `heroi_convocacao` VALUES (1,1,1),(2,4,2),(3,3,3),(4,5,4);
/*!40000 ALTER TABLE `heroi_convocacao` ENABLE KEYS */;
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
  CONSTRAINT `fk_heroilocalizador_heroi` FOREIGN KEY (`idheroi`) REFERENCES `heroi` (`idheroi`),
  CONSTRAINT `fk_heroilocalizador_localizador` FOREIGN KEY (`idlocalizador`) REFERENCES `localizador` (`idlocalizador`)
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
  CONSTRAINT `fk_heroitornozeleira_heroi` FOREIGN KEY (`idheroi`) REFERENCES `heroi` (`idheroi`),
  CONSTRAINT `fk_heroitornozeleira_tornozeleira` FOREIGN KEY (`idtornozeleira`) REFERENCES `tornozeleira` (`idtornozeleira`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `heroi_tornozeleira`
--

LOCK TABLES `heroi_tornozeleira` WRITE;
/*!40000 ALTER TABLE `heroi_tornozeleira` DISABLE KEYS */;
INSERT INTO `heroi_tornozeleira` VALUES (1,1,1),(3,5,3);
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
  `status_tornozeleira` enum('Ativa','Inativa') NOT NULL DEFAULT 'Inativa',
  `data_ativacao` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `data_desativacao` datetime DEFAULT NULL,
  PRIMARY KEY (`idtornozeleira`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tornozeleira`
--

LOCK TABLES `tornozeleira` WRITE;
/*!40000 ALTER TABLE `tornozeleira` DISABLE KEYS */;
INSERT INTO `tornozeleira` VALUES (1,'Ativa','2024-12-04 13:12:17',NULL),(3,'Ativa','2024-12-04 13:31:47',NULL);
/*!40000 ALTER TABLE `tornozeleira` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `view_herois_convocados`
--

DROP TABLE IF EXISTS `view_herois_convocados`;
/*!50001 DROP VIEW IF EXISTS `view_herois_convocados`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `view_herois_convocados` AS SELECT 
 1 AS `nome_heroi`,
 1 AS `data_convocacao`,
 1 AS `condicao`*/;
SET character_set_client = @saved_cs_client;

--
-- Dumping events for database 'vingadores'
--

--
-- Dumping routines for database 'vingadores'
--

--
-- Final view structure for view `view_herois_convocados`
--

/*!50001 DROP VIEW IF EXISTS `view_herois_convocados`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `view_herois_convocados` AS select `h`.`nome_heroi` AS `nome_heroi`,`c`.`data_convocacao` AS `data_convocacao`,`c`.`status_convocacao` AS `condicao` from ((`heroi_convocacao` `hc` join `heroi` `h` on((`h`.`idheroi` = `hc`.`idheroi`))) join `convocacao` `c` on((`c`.`idconvocacao` = `hc`.`idconvocacao`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-04 13:49:09

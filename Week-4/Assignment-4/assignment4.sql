-- MySQL dump 10.13  Distrib 8.3.0, for macos14 (arm64)
--
-- Host: localhost    Database: assignment
-- ------------------------------------------------------
-- Server version	8.3.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `assignment`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `assignment` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `assignment`;

--
-- Table structure for table `article`
--

DROP TABLE IF EXISTS `article`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `article` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `content` longtext,
  `author` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `author` (`author`),
  CONSTRAINT `article_ibfk_1` FOREIGN KEY (`author`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `article`
--

LOCK TABLES `article` WRITE;
/*!40000 ALTER TABLE `article` DISABLE KEYS */;
INSERT INTO `article` VALUES (2,'Test title 1','This is the first article created by author ID 13',13),(3,'Test title 2','This is the second article created by author ID 13',13),(4,'Test title 3','This is the third article created by author ID 13',13),(5,'Test title 4','This is the fourth artic\nle created by author ID 13',13),(6,'Test title 5','This is the fifth article created by author ID 13',13),(7,'Test title 6','This is the sixth article\n created by author ID 13',13),(8,'Test title 7','This is the first article created by author ID 14',14),(9,'Test title 8','This is the second article\ncreated by author ID 14',14),(10,'Test title 9','This is the third article created by author ID 14',14),(11,'Test title 10','This is the fourth article\ncreated by author ID 14',14),(12,'Test title 11','This is the fifth article created by author ID 14',14),(13,'Test title 12','This is the sixth article\ncreated by author ID 14',14),(14,'Test title 13','This is the first article created by author ID 15',15),(15,'Test title 14','This is the second article\n created by author ID 15',15),(16,'Test title 15','This is the third article created by author ID 15',15),(17,'Test title 16','This is the fourth articl\ne created by author ID 15',15),(18,'Test title 17','This is the fifth article created by author ID 15',15),(19,'Test title 18','This is the sixth articl\ne created by author ID 15',15),(20,'Test title 19','This is the first article created by author ID 16',16),(21,'Test title 20','This is the second artic\nle created by author ID 16',16),(22,'Test title 21','This is the third article created by author ID 16',16),(23,'Test title 22','This is the fourth arti\ncle created by author ID 16',16),(24,'Test title 23','This is the fifth article created by author ID 16',16),(25,'Test title 24','This is the sixth article created by author ID 16',16),(26,'Test title 25','This is the first article created by author ID 17',17),(27,'Test title 26','This is the second art\nicle created by author ID 17',17),(28,'Test title 27','This is the third article created by author ID 17',17),(29,'Test title 28','This is the fourth article created by author ID 17',17),(30,'Test title 29','This is the fifth article created by author ID 17',17),(31,'Test title 30','This is the sixth article created by author ID 17',17);
/*!40000 ALTER TABLE `article` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(64) NOT NULL,
  `password` varchar(64) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (13,'test1@gmail.com','$2b$12$Syt9iD8HEceryhVgxAmgpunCxppC4mNHBlf/k86iU6O3Oe.DqVSJ.'),(14,'test2@gmail.com','$2b$12$r.L50jfYAsKe84o4qYMpf.KMdw0K7SqvNFq.6kC0mceY5BxQsCjV6'),(15,'test3@gmail.com','$2b$12$7J34kgmGbhACOVlx8GLxUuGxRFnNijfgg9h50i5eo0Z76RqV8YcyS'),(16,'test4@gmail.com','$2b$12$5fPNbaI9eysLrLDrNuw2t.CQG7kNWelI3It6DJjiZ4KN/LyZIaQQ6'),(17,'test5@gmail.com','$2b$12$50uP9cHPWovyVQfx98BD4.y2lQHPXjV3WHCN47w.gRlNAsvUaBp6e');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-02-02 19:49:21


-- 1. Write an SQL statement to select all articles with their author’s email.
SELECT article.content, user.email FROM article INNER JOIN user ON article.author = user.id;
-- 2. Write another SQL statement to select articles from 7th to 12th sorted by id.
SELECT * FROM article WHERE id BETWEEN 7 AND 12;
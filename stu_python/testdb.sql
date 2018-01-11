-- MySQL dump 10.13  Distrib 5.5.41, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: testdb
-- ------------------------------------------------------
-- Server version	5.5.41-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Course`
--

DROP TABLE IF EXISTS `Course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Course` (
  `Cno` char(4) NOT NULL,
  `Cname` char(20) DEFAULT NULL,
  `Cpno` char(4) DEFAULT NULL,
  `Ccredit` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`Cno`),
  KEY `Cpno` (`Cpno`),
  CONSTRAINT `Course_ibfk_1` FOREIGN KEY (`Cpno`) REFERENCES `Course` (`Cno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Course`
--

LOCK TABLES `Course` WRITE;
/*!40000 ALTER TABLE `Course` DISABLE KEYS */;
INSERT INTO `Course` VALUES ('1','数据库','5',4),('2','数学',NULL,2),('3','信息系统','1',4),('4','操作系统','6',3),('5','数据结构','7',4),('6','数据处理',NULL,2),('7','PASCAL语言','6',4);
/*!40000 ALTER TABLE `Course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SC`
--

DROP TABLE IF EXISTS `SC`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `SC` (
  `Sno` char(9) NOT NULL DEFAULT '',
  `Cno` char(9) NOT NULL DEFAULT '',
  `Grade` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`Sno`,`Cno`),
  KEY `Cno` (`Cno`),
  CONSTRAINT `SC_ibfk_1` FOREIGN KEY (`Sno`) REFERENCES `Student` (`Sno`),
  CONSTRAINT `SC_ibfk_2` FOREIGN KEY (`Cno`) REFERENCES `Course` (`Cno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SC`
--

LOCK TABLES `SC` WRITE;
/*!40000 ALTER TABLE `SC` DISABLE KEYS */;
INSERT INTO `SC` VALUES ('20150001','1',92),('20150002','2',85),('20150003','3',88),('20150004','4',70),('20150005','5',59),('20150006','1',40),('20150007','2',100),('20150008','6',65);
/*!40000 ALTER TABLE `SC` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Student`
--

DROP TABLE IF EXISTS `Student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Student` (
  `Sno` char(9) NOT NULL,
  `Sname` char(20) DEFAULT NULL,
  `Ssex` char(8) DEFAULT NULL,
  `Sage` smallint(6) DEFAULT NULL,
  `Sdept` char(20) DEFAULT NULL,
  PRIMARY KEY (`Sno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Student`
--

LOCK TABLES `Student` WRITE;
/*!40000 ALTER TABLE `Student` DISABLE KEYS */;
INSERT INTO `Student` VALUES ('20150001','李全蛋','女',18,'MA'),('20150002','李能','男',20,'IS'),('20150003','节是','男',20,'IS'),('20150004','唐马濡','女',18,'CS'),('20150005','李勇','男',21,'MA'),('20150006','白素','女',16,'CS'),('20150007','王晶','男',19,'MA'),('20150008','丁一','男',20,'IS');
/*!40000 ALTER TABLE `Student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t1`
--

DROP TABLE IF EXISTS `t1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t1` (
  `id` int(11) NOT NULL DEFAULT '0',
  `name` varchar(8) DEFAULT NULL,
  `pid` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `pid` (`pid`),
  CONSTRAINT `t1_ibfk_1` FOREIGN KEY (`pid`) REFERENCES `t1` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t1`
--

LOCK TABLES `t1` WRITE;
/*!40000 ALTER TABLE `t1` DISABLE KEYS */;
INSERT INTO `t1` VALUES (1,'aa',NULL),(2,'aa',1);
/*!40000 ALTER TABLE `t1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb1`
--

DROP TABLE IF EXISTS `tb1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb1` (
  `Text` char(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb1`
--

LOCK TABLES `tb1` WRITE;
/*!40000 ALTER TABLE `tb1` DISABLE KEYS */;
INSERT INTO `tb1` VALUES ('aaa'),('ä½ å¥½'),('ä½ å¥½'),('ä½ å¥½'),('ä½ å¥½'),('你好'),('ä½ å¥½'),('ä½ å¥½111'),('你好111');
/*!40000 ALTER TABLE `tb1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb2`
--

DROP TABLE IF EXISTS `tb2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb2` (
  `id` int(11) DEFAULT NULL,
  `name` char(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb2`
--

LOCK TABLES `tb2` WRITE;
/*!40000 ALTER TABLE `tb2` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb2` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-02-09 14:59:17

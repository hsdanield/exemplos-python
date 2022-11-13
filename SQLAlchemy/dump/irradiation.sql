CREATE DATABASE IF NOT EXISTS dev;

USE dev;

CREATE TABLE
    IF NOT EXISTS `tb_country` (
  `id_country` int NOT NULL AUTO_INCREMENT,
  `initials` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `dt_create` datetime DEFAULT CURRENT_TIMESTAMP,
  `dt_update` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_country`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;


CREATE TABLE `tb_state` (
  `id_state` int NOT NULL AUTO_INCREMENT,
  `ibge_code` int DEFAULT NULL,
  `initials` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `dt_create` datetime DEFAULT CURRENT_TIMESTAMP,
  `dt_update` datetime DEFAULT CURRENT_TIMESTAMP,
  `id_country` int DEFAULT NULL,
  PRIMARY KEY (`id_state`),
  KEY `fk_state_country` (`id_country`),
  CONSTRAINT `fk_state_country` FOREIGN KEY (`id_country`) REFERENCES `tb_country` (`id_country`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;


INSERT INTO `tb_country` VALUES (1,'BR','Brazil','2022-08-08 18:05:17','2022-08-08 18:05:18');
COMMIT;

INSERT INTO `tb_state` VALUES (1,12,'AC','Acre','2022-08-08 18:05:37','2022-08-08 18:05:39',1),(2,27,'AL','Alagoas','2022-08-08 18:05:37','2022-08-08 18:05:39',1),(3,16,'AP','Amapá','2022-08-08 18:05:37','2022-08-08 18:05:39',1),(4,13,'AM','Amazonas','2022-08-08 18:05:37','2022-08-08 18:05:39',1),(5,29,'BA','Bahia','2022-08-08 18:05:37','2022-08-08 18:05:39',1),(6,23,'CE','Ceará','2022-08-08 18:05:37','2022-08-08 18:05:39',1),(7,53,'DF','Distrito Federal','2022-08-08 18:05:37','2022-08-08 18:05:39',1),(8,32,'ES','Espírito Santo','2022-08-08 18:05:37','2022-08-08 18:05:39',1),(9,52,'GO','Goiás','2022-08-08 18:05:37','2022-08-08 18:05:39',1),(10,21,'MA','Maranhão','2022-08-08 18:05:37','2022-08-08 18:05:39',1),(11,51,'MT','Mato Grosso','2022-08-08 18:05:37','2022-08-08 18:05:39',1),(12,50,'MS','Mato Grosso do Sul','2022-08-08 18:05:37','2022-08-08 18:05:39',1),(13,31,'MG','Minas Gerais','2022-08-08 18:05:37','2022-08-08 18:05:39',1),(14,15,'PA','Pará','2022-08-08 18:05:37','2022-08-08 18:05:39',1),(15,25,'PB','Paraíba','2022-08-08 18:05:37','2022-08-08 18:05:39',1),(16,41,'PR','Paraná','2022-08-08 18:05:37','2022-08-08 18:05:39',1),(17,26,'PE','Pernambuco','2022-08-08 18:05:37','2022-08-08 18:05:39',1),(18,22,'PI','Piauí','2022-08-08 18:05:37','2022-08-08 18:05:39',1),(19,33,'RJ','Rio de Janeiro','2022-08-08 18:05:37','2022-08-08 18:05:39',1),(20,24,'RN','Rio Grande do Norte','2022-08-08 18:05:37','2022-08-08 18:05:39',1),(21,43,'RS','Rio Grande do Sul','2022-08-08 18:05:37','2022-08-08 18:05:39',1),(22,11,'RO','Rondônia','2022-08-08 18:05:37','2022-08-08 18:05:39',1),(23,14,'RR','Roraima','2022-08-08 18:05:37','2022-08-08 18:05:39',1),(24,42,'SC','Santa Catarina','2022-08-08 18:05:37','2022-08-08 18:05:39',1),(25,35,'SP','São Paulo','2022-08-08 18:05:37','2022-08-08 18:05:39',1),(26,28,'SE','Sergipe','2022-08-08 18:05:37','2022-08-08 18:05:39',1),(27,17,'TO','Tocantins','2022-08-08 18:05:37','2022-08-08 18:05:39',1);

COMMIT;
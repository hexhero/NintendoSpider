/*
Navicat MySQL Data Transfer

Source Server         : 47.111.99.248
Source Server Version : 50643
Source Host           : 47.111.99.248:3306
Source Database       : yhh_game

Target Server Type    : MYSQL
Target Server Version : 50643
File Encoding         : 65001

Date: 2019-04-28 10:07:26
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for GAME_INFO
-- ----------------------------
DROP TABLE IF EXISTS `GAME_INFO`;
CREATE TABLE `GAME_INFO` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `platform` varchar(32) COLLATE utf8mb4_bin DEFAULT '' COMMENT '平台',
  `title` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '游戏名称',
  `title_zh` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '中文标题',
  `release_date` date DEFAULT NULL COMMENT '发行日期',
  `best_price` int(11) DEFAULT NULL COMMENT '是否有优惠',
  `current_price` decimal(16,2) DEFAULT NULL COMMENT '当前价格',
  `status` varchar(11) COLLATE utf8mb4_bin DEFAULT NULL,
  `url_eshop` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '商城链接',
  `discount` int(11) DEFAULT NULL COMMENT '是否有打折',
  `country_code` varchar(8) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '国家代码',
  `country_name` varchar(64) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '国家名称',
  `regular_price` decimal(16,2) DEFAULT NULL COMMENT '原价',
  `discount_price` decimal(16,2) DEFAULT NULL COMMENT '折扣价',
  `discount_begin` date DEFAULT NULL COMMENT '折扣开始日期',
  `discount_end` date DEFAULT NULL COMMENT '折扣结束日期',
  `spider_time` date DEFAULT NULL,
  `percentOff` varchar(10) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '折扣率',
  `image_url` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '游戏图片链接',
  `data_source` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '数据来源',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1455 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

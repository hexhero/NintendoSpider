/*
Navicat MySQL Data Transfer


Source Server Version : 50643

Target Server Type    : MYSQL
Target Server Version : 50643
File Encoding         : 65001

Date: 2019-09-17 12:22:57
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for game
-- ----------------------------
DROP TABLE IF EXISTS `game`;
CREATE TABLE `game` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `content` varchar(1024) DEFAULT NULL COMMENT '游戏介绍',
  `capacity` varchar(32) DEFAULT NULL COMMENT '容量',
  `player` varchar(32) DEFAULT NULL COMMENT '玩家人数',
  `cassette` varchar(32) DEFAULT NULL COMMENT '实体卡带',
  `demo` varchar(32) DEFAULT NULL COMMENT '试玩',
  `remark` varchar(1024) DEFAULT NULL COMMENT '备注(评论,评分等)',
  `ids_tag` varchar(128) DEFAULT NULL COMMENT '标签id集合',
  `ids_tag_name` varchar(128) DEFAULT NULL COMMENT '标签名称集合',
  `ids_category` varchar(128) DEFAULT NULL COMMENT '分类id集合',
  `ids_category_name` varchar(128) DEFAULT NULL COMMENT '分类名称集合',
  `files_path` varchar(1024) DEFAULT NULL COMMENT '封面文件路径',
  `img_files_path` varchar(1024) DEFAULT NULL COMMENT '图片路径集合(逗号分隔)',
  `video_files_path` varchar(1024) DEFAULT NULL COMMENT '视频路径集合(逗号分隔)',
  `status` smallint(6) DEFAULT NULL COMMENT '状态(数据)',
  `top` smallint(6) DEFAULT NULL COMMENT '是否置顶',
  `org_code` varchar(32) DEFAULT NULL COMMENT '机构编码',
  `create_user` bigint(20) DEFAULT NULL COMMENT '创建人ID',
  `create_username` varchar(32) DEFAULT NULL COMMENT '创建人姓名',
  `create_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_user` bigint(20) DEFAULT NULL COMMENT '修改人',
  `update_date` timestamp NULL DEFAULT NULL COMMENT '修改时间',
  `platform` varchar(32) DEFAULT NULL COMMENT '平台',
  `title` varchar(255) DEFAULT NULL COMMENT '游戏名称',
  `title_zh` varchar(255) DEFAULT NULL COMMENT '中文标题',
  `release_date` timestamp NULL DEFAULT NULL COMMENT '发行日期',
  `best_price` int(11) DEFAULT NULL COMMENT '是否有优惠',
  `current_price` decimal(16,2) DEFAULT NULL COMMENT '当前价格',
  `url_eshop` varchar(255) DEFAULT NULL COMMENT '商城链接',
  `discount` int(11) DEFAULT NULL COMMENT '是否有打折',
  `country_code` varchar(8) DEFAULT NULL COMMENT '国家代码',
  `country_name` varchar(64) DEFAULT NULL COMMENT '国家名称',
  `regular_price` decimal(16,2) DEFAULT NULL COMMENT '原价',
  `discount_price` decimal(16,2) DEFAULT NULL COMMENT '折扣价',
  `discount_begin` timestamp NULL DEFAULT NULL COMMENT '折扣开始日期',
  `discount_end` timestamp NULL DEFAULT NULL COMMENT '折扣结束日期',
  `spider_time` timestamp NULL DEFAULT NULL COMMENT '爬虫日期',
  `percentOff` varchar(10) DEFAULT NULL COMMENT '折扣率',
  `image_url` varchar(255) DEFAULT NULL COMMENT '游戏图片链接',
  `data_source` varchar(255) DEFAULT NULL COMMENT '数据来源',
  `prices` text COMMENT '价格信息',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2935 DEFAULT CHARSET=utf8 COMMENT='游戏表';

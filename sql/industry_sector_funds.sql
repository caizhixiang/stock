/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 80019
 Source Host           : localhost:3306
 Source Schema         : stock

 Target Server Type    : MySQL
 Target Server Version : 80019
 File Encoding         : 65001

 Date: 17/05/2021 02:42:48
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for industry_sector_funds
-- ----------------------------
DROP TABLE IF EXISTS `industry_sector_funds`;
CREATE TABLE `industry_sector_funds`  (
  `id` int(0) NOT NULL COMMENT '主键id',
  `up_and_down` decimal(5, 2) NULL DEFAULT NULL COMMENT '涨跌幅',
  `symbol` varchar(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '符号(+/-)',
  `turnover_rate` decimal(5, 2) NULL DEFAULT NULL COMMENT '换手率',
  `rising_nums` int(0) NULL DEFAULT NULL COMMENT '上涨家数',
  `decliner_nums` int(0) NULL DEFAULT NULL COMMENT '下跌家数',
  `leading_stock` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '领涨股票',
  `inflows` decimal(10, 2) NULL DEFAULT NULL COMMENT '资金净流入',
  `ranking` int(0) NULL DEFAULT NULL COMMENT '排名',
  `create_time` datetime(0) NULL DEFAULT NULL COMMENT '创建日期',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '板块涨幅' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for industry_stock
-- ----------------------------
DROP TABLE IF EXISTS `industry_stock`;
CREATE TABLE `industry_stock`  (
  `id` int(0) NOT NULL COMMENT '主键id',
  `stock_code` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '股票编码',
  `stock_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '股票名称',
  `abridge` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '拼音简写',
  `industry_code` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '所属行业',
  `concept` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '所属概念',
  `create_time` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '股票-行业关系' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for news
-- ----------------------------
DROP TABLE IF EXISTS `news`;
CREATE TABLE `news`  (
  `id` int(0) NOT NULL COMMENT '主键id',
  `introduction` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '简介',
  `href` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '文章地址',
  `keys` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '关键字',
  `industry` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '所属行业',
  `create_time` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '新闻' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for stock_daily
-- ----------------------------
DROP TABLE IF EXISTS `stock_daily`;
CREATE TABLE `stock_daily`  (
  `id` int(0) NOT NULL AUTO_INCREMENT COMMENT '主键id',
  `stock_code` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '股票代码',
  `up_and_down` decimal(5, 2) NULL DEFAULT NULL COMMENT '涨跌幅',
  `symbol` varchar(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '符号',
  `turnover_rate` decimal(5, 2) NULL DEFAULT NULL COMMENT '换手率',
  `inflows` decimal(10, 2) NULL DEFAULT NULL COMMENT '资金净流入',
  `create_time` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '股票日常走势' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for stock_fundamental
-- ----------------------------
DROP TABLE IF EXISTS `stock_fundamental`;
CREATE TABLE `stock_fundamental`  (
  `id` int(0) NOT NULL COMMENT '主键id',
  `profit` decimal(10, 2) NULL DEFAULT NULL COMMENT '净利润',
  `profit_rate` decimal(10, 2) NULL DEFAULT NULL COMMENT '毛利率',
  `controller` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '实际控制人',
  `shareholders` int(0) NULL DEFAULT NULL COMMENT '股东人数(W)',
  `per_capita` int(0) NULL DEFAULT NULL COMMENT '人均持股数(W)',
  `convergence_rate` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '筹码集中度',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '股票基本面' ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;

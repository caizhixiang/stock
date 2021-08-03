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

 Date: 03/08/2021 07:56:54
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for industry_info
-- ----------------------------
DROP TABLE IF EXISTS `industry_info`;
CREATE TABLE `industry_info`  (
  `id` int(0) NOT NULL AUTO_INCREMENT COMMENT '主键id',
  `name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '行业名称',
  `code` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '行业编码',
  `sector_link` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '行业板块（板块资金）',
  `quotation_link` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '行情（偏向资讯）',
  `create_time` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  `update_time` datetime(0) NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 62 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '行业信息' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for industry_sector_funds
-- ----------------------------
DROP TABLE IF EXISTS `industry_sector_funds`;
CREATE TABLE `industry_sector_funds`  (
  `id` int(0) NOT NULL AUTO_INCREMENT COMMENT '主键id',
  `industry_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '板块名称',
  `industry_code` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '板块code',
  `open` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '开盘价',
  `close` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '收盘价',
  `high` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '最高价',
  `low` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '最低价',
  `preclose` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '前收盘价',
  `volume` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '成交量（累计 单位：股）',
  `amount` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '成交额',
  `inner` int(0) NULL DEFAULT NULL COMMENT '内盘',
  `outer` int(0) NULL DEFAULT NULL COMMENT '外盘',
  `peTTM` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '流通市值	',
  `pctChg` decimal(5, 2) NULL DEFAULT NULL COMMENT '涨跌幅',
  `amplitude` decimal(5, 2) NULL DEFAULT NULL COMMENT '振幅',
  `turn` decimal(5, 2) NULL DEFAULT NULL COMMENT '换手率',
  `rising_nums` int(0) NULL DEFAULT NULL COMMENT '上涨家数',
  `decliner_nums` int(0) NULL DEFAULT NULL COMMENT '下跌家数',
  `flat_nums` int(0) NULL DEFAULT NULL COMMENT '平家数',
  `leading_stock` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '领涨股票',
  `main_net_inflow` decimal(10, 5) NULL DEFAULT NULL COMMENT '主力资金净流入',
  `main_inflow` decimal(10, 5) NULL DEFAULT NULL COMMENT '主力流入',
  `main_outflow` decimal(10, 5) NULL DEFAULT NULL COMMENT '主力流出',
  `create_time` datetime(0) NULL DEFAULT NULL COMMENT '创建日期',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 123 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '板块涨幅+资金' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for industry_stock
-- ----------------------------
DROP TABLE IF EXISTS `industry_stock`;
CREATE TABLE `industry_stock`  (
  `id` int(0) NOT NULL COMMENT '主键id',
  `stock_code` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '股票编码',
  `stock_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '股票名称',
  `abridge` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '拼音简写',
  `industry_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '所属行业',
  `concept` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '所属概念',
  `stock_detail_url` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '股票详情地址',
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
  `create_time` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '股票基本面' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for stock_funds
-- ----------------------------
DROP TABLE IF EXISTS `stock_funds`;
CREATE TABLE `stock_funds`  (
  `id` int(0) NOT NULL AUTO_INCREMENT COMMENT '主键id',
  `stock_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '股票名称',
  `stock_code` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '股票编码',
  `open` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '开盘价',
  `close` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '收盘价',
  `high` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '最高价',
  `low` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '最低价',
  `preclose` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '前收盘价',
  `volume` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '成交量（累计 单位：股）',
  `amount` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '成交额',
  `adjustflag` tinyint(1) NULL DEFAULT NULL COMMENT '复权状态(1：后复权， 2：前复权，3：不复权）',
  `tradestatus` tinyint(1) NULL DEFAULT NULL COMMENT '交易状态(1：正常交易 0：停牌）',
  `peTTM` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '滚动市盈率	',
  `pctChg` decimal(5, 2) NULL DEFAULT NULL COMMENT '涨跌幅',
  `turn` decimal(5, 2) NULL DEFAULT NULL COMMENT '换手率',
  `rising_nums` int(0) NULL DEFAULT NULL COMMENT '上涨家数',
  `decliner_nums` int(0) NULL DEFAULT NULL COMMENT '下跌家数',
  `leading_stock` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '领涨股票',
  `main_net_inflow` decimal(10, 5) NULL DEFAULT NULL COMMENT '主力资金净流入',
  `super_large_inflow` decimal(10, 5) NULL DEFAULT NULL COMMENT '超级大单资金净流入',
  `large_inflow` decimal(10, 5) NULL DEFAULT NULL COMMENT '大单净流入',
  `middle_inflow` decimal(10, 5) NULL DEFAULT NULL COMMENT '中单净流入',
  `small_inflow` decimal(10, 5) NULL DEFAULT NULL COMMENT '小单净流入',
  `create_time` datetime(0) NULL DEFAULT NULL COMMENT '创建日期',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 162 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '股票每日涨幅+资金' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for stock_market
-- ----------------------------
DROP TABLE IF EXISTS `stock_market`;
CREATE TABLE `stock_market`  (
  `id` int(0) NOT NULL AUTO_INCREMENT COMMENT '主键id',
  `market_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '大盘名称',
  `market_code` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '大盘code',
  `open` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '开盘价',
  `close` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '收盘价',
  `high` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '最高价',
  `low` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '最低价',
  `preclose` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '前收盘价',
  `volume` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '成交量（累计 单位：股）',
  `amount` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '成交额',
  `inner` int(0) NULL DEFAULT NULL COMMENT '内盘',
  `outer` int(0) NULL DEFAULT NULL COMMENT '外盘',
  `peTTM` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '流通市值	',
  `pctChg` decimal(5, 2) NULL DEFAULT NULL COMMENT '涨跌幅',
  `amplitude` decimal(5, 2) NULL DEFAULT NULL COMMENT '振幅',
  `turn` decimal(5, 2) NULL DEFAULT NULL COMMENT '换手率',
  `rising_nums` int(0) NULL DEFAULT NULL COMMENT '上涨家数',
  `decliner_nums` int(0) NULL DEFAULT NULL COMMENT '下跌家数',
  `flat_nums` int(0) NULL DEFAULT NULL COMMENT '平家数',
  `leading_stock` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '领涨股票',
  `main_net_inflow` decimal(10, 5) NULL DEFAULT NULL COMMENT '主力资金净流入',
  `main_inflow` decimal(10, 5) NULL DEFAULT NULL COMMENT '主力流入',
  `main_outflow` decimal(10, 5) NULL DEFAULT NULL COMMENT '主力流出',
  `create_time` datetime(0) NULL DEFAULT NULL COMMENT '创建日期',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '板块涨幅+资金' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for template
-- ----------------------------
DROP TABLE IF EXISTS `template`;
CREATE TABLE `template`  (
  `id` int(0) NOT NULL AUTO_INCREMENT COMMENT '主键id',
  `industry_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '板块名称',
  `open` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '开盘价',
  `close` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '收盘价',
  `high` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '最高价',
  `low` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '最低价',
  `preclose` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '前收盘价',
  `volume` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '成交量（累计 单位：股）',
  `amount` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '成交额',
  `adjustflag` tinyint(1) NULL DEFAULT NULL COMMENT '复权状态(1：后复权， 2：前复权，3：不复权）',
  `tradestatus` tinyint(1) NULL DEFAULT NULL COMMENT '交易状态(1：正常交易 0：停牌）',
  `peTTM` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '滚动市盈率	',
  `pctChg` decimal(5, 2) NULL DEFAULT NULL COMMENT '涨跌幅',
  `turn` decimal(5, 2) NULL DEFAULT NULL COMMENT '换手率',
  `rising_nums` int(0) NULL DEFAULT NULL COMMENT '上涨家数',
  `decliner_nums` int(0) NULL DEFAULT NULL COMMENT '下跌家数',
  `leading_stock` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '领涨股票',
  `main_net_inflow` decimal(10, 5) NULL DEFAULT NULL COMMENT '主力资金净流入',
  `super_large_inflow` decimal(10, 5) NULL DEFAULT NULL COMMENT '超级大单资金净流入',
  `large_inflow` decimal(10, 5) NULL DEFAULT NULL COMMENT '大单净流入',
  `middle_inflow` decimal(10, 5) NULL DEFAULT NULL COMMENT '中单净流入',
  `small_inflow` decimal(10, 5) NULL DEFAULT NULL COMMENT '小单净流入',
  `create_time` datetime(0) NULL DEFAULT NULL COMMENT '创建日期',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '板块涨幅+资金' ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;

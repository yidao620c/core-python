CREATE DATABASE IF NOT EXISTS tobacco default charset utf8 COLLATE utf8_general_ci;

-- 导购员表
DROP TABLE IF EXISTS t_sales;
CREATE TABLE t_sales (
  id                BIGINT PRIMARY KEY AUTO_INCREMENT COMMENT '主键ID',
  username          VARCHAR(32) NOT NULL COMMENT '用户名',
  password          VARCHAR(64) COMMENT '密码',
  fullname          VARCHAR(10) COMMENT '中文名',
  allocated         SMALLINT DEFAULT 0 COMMENT '是否分配 0:未分配 1:已分配',
  area               VARCHAR(30) DEFAULT 'chongqing' COMMENT '所属片区',
  created_time      DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  updated_time      DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间'
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT '导购员表';

-- 活动配置表
DROP TABLE IF EXISTS t_lottery_config;
CREATE TABLE t_lottery_config (
  id                 BIGINT PRIMARY KEY AUTO_INCREMENT COMMENT '主键ID',
  area               VARCHAR(30) DEFAULT 'chongqing' COMMENT '所属片区',
  name               VARCHAR(255) COMMENT '活动名',
  start_time        VARCHAR(255) COMMENT '开始时间',
  end_time          VARCHAR(255) COMMENT '结束时间',
  icon               VARCHAR(255) DEFAULT 'icon.png' COMMENT '图标名称',
  homepic           VARCHAR(255) DEFAULT 'homepic.png' COMMENT '首页图片名称',
  regular           TEXT COMMENT '活动规则',
  valid             SMALLINT DEFAULT 1 COMMENT '是否有效',
  created_time      DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  updated_time      DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间'
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT '活动配置表';

-- 抽奖项表
DROP TABLE IF EXISTS t_lottery_item;
CREATE TABLE t_lottery_item (
  id                 BIGINT PRIMARY KEY AUTO_INCREMENT COMMENT '主键ID',
  config_id         BIGINT COMMENT '配置ID',
  money              INTEGER COMMENT '返点金额（分）',
  probability       VARCHAR(10) COMMENT '概率(比如0.2)',
  created_time      DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  updated_time      DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间'
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT '抽奖项表';

-- 渠道表
DROP TABLE IF EXISTS t_channel;
CREATE TABLE t_channel (
  id                BIGINT PRIMARY KEY AUTO_INCREMENT COMMENT '主键ID',
  name              VARCHAR(255) COMMENT '渠道名称',
  config_id         BIGINT COMMENT '配置ID',
  sales_id          BIGINT COMMENT '导购员ID',
  created_time      DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  updated_time      DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间'
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT '渠道表';

-- 抽奖记录表
DROP TABLE IF EXISTS t_lottery;
CREATE TABLE t_lottery (
  id                       BIGINT PRIMARY KEY AUTO_INCREMENT COMMENT '主键ID',
  openid                   VARCHAR(255) NOT NULL COMMENT '用户openid',
  phone                    VARCHAR(20) COMMENT '用户手机号',
  channel_id               BIGINT COMMENT '渠道ID',
  active                   SMALLINT DEFAULT 0 COMMENT '是否有效 0:无效 1:有效',
  start                    SMALLINT DEFAULT 1 COMMENT '开启新一轮 0:否 1:是',
  lucky_count              INTEGER DEFAULT 0 COMMENT '用户本次抽奖次数',
  lucky_money              INTEGER DEFAULT 0 COMMENT '用户本次抽奖金额（分）',
  scan_count_total        INTEGER DEFAULT 0 COMMENT '用户扫码总次数',
  lucky_count_total       INTEGER DEFAULT 0 COMMENT '用户抽奖总次数',
  lucky_money_total       INTEGER DEFAULT 0 COMMENT '用户抽奖总金额（分）',
  valid                     SMALLINT DEFAULT 1 COMMENT '是否有效',
  created_time             DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  updated_time             DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间'
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT '抽奖记录表';

-- 抽奖订单表
DROP TABLE IF EXISTS t_lottery_order;
CREATE TABLE t_lottery_order (
  id                       BIGINT PRIMARY KEY AUTO_INCREMENT COMMENT '主键ID',
  channel_id              BIGINT NOT NULl COMMENT '渠道ID',
  orderid                  VARCHAR(255) NOT NULL COMMENT '订单号',
  phone                    VARCHAR(255) NOT NULL COMMENT '用户手机号',
  lucky_money              INTEGER DEFAULT 0 COMMENT '用户本次抽奖金额（分）',
  created_time             DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  updated_time             DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间'
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT '抽奖订单表';

-- 用户表
DROP TABLE IF EXISTS t_user;
CREATE TABLE t_user (
  id                BIGINT PRIMARY KEY AUTO_INCREMENT COMMENT '主键ID',
  username          VARCHAR(32) NOT NULL COMMENT '用户名',
  password          VARCHAR(64) COMMENT '密码',
  fullname          VARCHAR(10) COMMENT '中文名',
  mobile            VARCHAR(20) COMMENT '联系电话',
  role              SMALLINT COMMENT '角色 0:系统管理员 1:市公司管理员 2:终端维护员 3:终端店主',
  area              VARCHAR(30) COMMENT '所属片区',
  created_time      DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  updated_time      DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间'
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT '用户表';


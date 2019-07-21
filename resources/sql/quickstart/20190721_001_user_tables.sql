-- ************************************** `user`
CREATE TABLE IF NOT EXISTS `{$NAMESPACE}`.`user`
(
  `id`              INT(10) unsigned NOT NULL AUTO_INCREMENT,
  `sid`             VARBINARY(64) NOT NULL,
  `userName`        VARCHAR(64) NOT NULL,
  `realName`        VARCHAR(128) NOT NULL,
  `dateCreated`     INT(10) unsigned NOT NULL,
  `dateModified`    INT(10) unsigned NOT NULL,
  `isSystemAgent`   TINYINT NOT NULL,
  `isDisabled`      TINYINT NOT NULL,
  `isAdmin`         TINYINT NOT NULL,
  `isEmailVerified` INT(10) unsigned NOT NULL,
  `isApproved`       INT(10) unsigned NOT NULL,

  PRIMARY KEY (`id`),
  UNIQUE KEY `userName` (`userName`),
  UNIQUE KEY `sid` (`sid`),
  KEY `realName` (`realName`),
  KEY `key_approved` (`isApproved`)
) ENGINE=InnoDB DEFAULT CHARSET={$CHARSET_DEFAULT} COLLATE={$COLLATE_TEXT};


-- ************************************** `user_profile`
CREATE TABLE IF NOT EXISTS `{$NAMESPACE}`.`user_profile` (
  `id`           INT(10) unsigned NOT NULL AUTO_INCREMENT,
  `userSID`      VARBINARY(64) NOT NULL,
  `title`        VARCHAR(255),
  `blurb`        LONGTEXT COLLATE {$COLLATE_TEXT},
  `dateCreated`  INT(10) unsigned NOT NULL,
  `dateModified` INT(10) unsigned NOT NULL,

  PRIMARY KEY (`id`),
  UNIQUE KEY `userSID` (`userSID`)
) ENGINE=InnoDB DEFAULT CHARSET={$CHARSET_DEFAULT} COLLATE={$COLLATE_TEXT};


-- ************************************** `user_preferences`
CREATE TABLE IF NOT EXISTS `{$NAMESPACE}`.`user_preferences` (
  `id`          INT(10) unsigned NOT NULL AUTO_INCREMENT,
  `sid`         VARBINARY(64) NOT NULL,
  `userSID`     VARBINARY(64) NOT NULL,
  `preferences` LONGTEXT COLLATE {$COLLATE_TEXT} NOT NULL,
  `dateCreated` INT(10) unsigned NOT NULL,
  `datModified` INT(10) unsigned NOT NULL,

  PRIMARY KEY (`id`),
  UNIQUE KEY `key_sid` (`sid`),
  UNIQUE KEY `key_user` (`userSID`)
) ENGINE=InnoDB DEFAULT CHARSET={$CHARSET_DEFAULT} COLLATE={$COLLATE_TEXT};


-- ************************************** `user_log`
CREATE TABLE IF NOT EXISTS `{$NAMESPACE}`.`user_log` (
  `id`           INT(10) unsigned NOT NULL AUTO_INCREMENT,
  `userSID`      VARBINARY(64) NOT NULL,
  `actorSID`     VARBINARY(64) NOT NULL,
  `action`       VARCHAR(64) NOT NULL,
  `oldValue`     LONGTEXT COLLATE {$COLLATE_TEXT} NOT NULL,
  `newValue`     LONGTEXT COLLATE {$COLLATE_TEXT} NOT NULL,
  `details`      LONGTEXT COLLATE {$COLLATE_TEXT} NOT NULL,
  `dateCreated`  INT(10) unsigned NOT NULL,
  `dateModified` INT(10) unsigned NOT NULL,
  `remoteAddr`   VARCHAR(64) NOT NULL,
  `session`      BINARY,

  PRIMARY KEY (`id`),
  KEY `actorSID` (`actorSID`,`dateCreated`),
  KEY `userSID` (`userSID`,`dateCreated`),
  KEY `action` (`action`,`dateCreated`),
  KEY `dateCreated` (`dateCreated`),
  KEY `remoteAddr` (`remoteAddr`,`dateCreated`),
  KEY `session` (`session`,`dateCreated`)
) ENGINE=InnoDB DEFAULT CHARSET={$CHARSET_DEFAULT} COLLATE={$COLLATE_TEXT};


-- ************************************** `user_email`
CREATE TABLE IF NOT EXISTS `{$NAMESPACE}`.`user_email` (
  `id`               INT(10) unsigned NOT NULL AUTO_INCREMENT,
  `userSID`          VARBINARY(64) NOT NULL,
  `address`          VARCHAR(128) NOT NULL,
  `isVerified`       TINYINT NOT NULL,
  `isPrimary`        TINYINT NOT NULL,
  `verificationCode` VARCHAR(64) NOT NULL,
  `dateCreated`      INT(10) unsigned NOT NULL,
  `dateModified`     INT(10) unsigned NOT NULL,

  PRIMARY KEY (`id`),
  UNIQUE KEY `address` (`address`),
  KEY `userSID` (`userSID`,`isPrimary`)
) ENGINE=InnoDB DEFAULT CHARSET={$CHARSET_DEFAULT} COLLATE={$COLLATE_TEXT};


-- ************************************** `user_session`
CREATE TABLE IF NOT EXISTS `{$NAMESPACE}`.`user_session` (
  `id`             INT(10) unsigned NOT NULL AUTO_INCREMENT,
  `userSID`        VARBINARY(64) NOT NULL,
  `type`           VARCHAR(32) NOT NULL,
  `sessionKey`     BINARY NOT NULL,
  `sessionStart`   INT(10) unsigned NOT NULL,
  `sessionExpires` INT(10) unsigned NOT NULL,
  `isPartial`      TINYINT NOT NULL,

  PRIMARY KEY (`id`),
  UNIQUE KEY `sessionKey` (`sessionKey`),
  KEY `key_identity` (`userSID`,`type`),
  KEY `key_expires` (`sessionExpires`)
) ENGINE=InnoDB DEFAULT CHARSET={$CHARSET_DEFAULT} COLLATE={$COLLATE_TEXT};

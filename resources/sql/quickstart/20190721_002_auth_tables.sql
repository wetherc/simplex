-- ************************************** `auth_providerconfig`
CREATE TABLE IF NOT EXISTS `{$NAMESPACE}`.`auth_providerconfig` (
  `id`                      INT(10) unsigned NOT NULL AUTO_INCREMENT,
  `sid`                     VARBINARY(64) NOT NULL,
  `providerClass`           VARCHAR(128) NOT NULL,
  `providerType`            VARCHAR(32) NOT NULL,
  `providerDomain`          VARCHAR(128) NOT NULL,
  `isEnabled`               TINYINT NOT NULL,
  `shouldAllowLogin`        TINYINT NOT NULL,
  `shouldAllowRegistration` TINYINT NOT NULL,
  `shouldAllowLink`         TINYINT NOT NULL,
  `shouldAllowUnlink`       TINYINT NOT NULL,
  `shouldTrustEmails`       TINYINT NOT NULL,
  `properties`              LONGTEXT COLLATE {$COLLATE_TEXT} NOT NULL,
  `dateCreated`             INT(10) unsigned NOT NULL,
  `dateModified`            INT(10) unsigned NOT NULL,
  `shouldAutoLogin`         TINYINT NOT NULL,

  PRIMARY KEY (`id`),
  UNIQUE KEY `key_sid` (`sid`),
  UNIQUE KEY `key_provider` (`providerType`,`providerDomain`),
  KEY `key_class` (`providerClass`)
) ENGINE=InnoDB DEFAULT CHARSET={$CHARSET_DEFAULT} COLLATE={$COLLATE_TEXT};


-- ************************************** `auth_providerconfigtransaction`
CREATE TABLE IF NOT EXISTS `{$NAMESPACE}`.`auth_providerconfigtransaction` (
  `id`               INT(10) unsigned NOT NULL AUTO_INCREMENT,
  `sid`              VARBINARY(64) NOT NULL,
  `authorSID`        VARBINARY(64) NOT NULL,
  `objectSID`        VARBINARY(64) NOT NULL,
  `viewPolicy`       VARBINARY(64) NOT NULL,
  `editPolicy`       VARBINARY(64) NOT NULL,
  `transactionType`  VARCHAR(32) NOT NULL,
  `oldValue`         LONGTEXT COLLATE {$COLLATE_TEXT} NOT NULL,
  `newValue`         LONGTEXT COLLATE {$COLLATE_TEXT} NOT NULL,
  `metadata`         LONGTEXT COLLATE {$COLLATE_TEXT} NOT NULL,
  `contentSource`    LONGTEXT COLLATE {$COLLATE_TEXT} NOT NULL,
  `dateCreated`      INT(10) unsigned NOT NULL,
  `dateModified`     INT(10) unsigned NOT NULL,

  PRIMARY KEY (`id`),
  UNIQUE KEY `key_sid` (`sid`),
  KEY `key_object` (`objectSID`)
) ENGINE=InnoDB DEFAULT CHARSET={$CHARSET_DEFAULT} COLLATE={$COLLATE_TEXT};


-- ************************************** `auth_temporarytoken`
CREATE TABLE IF NOT EXISTS `{$NAMESPACE}`.`auth_temporarytoken` (
  `id`            INT(10) unsigned NOT NULL AUTO_INCREMENT,
  `userSID`       VARBINARY(64) NOT NULL,
  `tokenResource` VARBINARY(64) NOT NULL,
  `tokenType`     VARCHAR(64) NOT NULL,
  `tokenExpires`  INT(10) unsigned NOT NULL,
  `tokenCode`     VARCHAR(64) NOT NULL,
  `properties`    LONGTEXT COLLATE {$COLLATE_TEXT} NOT NULL,

  PRIMARY KEY (`id`),
  UNIQUE KEY `key_token` (`tokenResource`,`tokenType`,`tokenCode`),
  KEY `key_expires` (`tokenExpires`),
  KEY `key_user` (`userSID`)
) ENGINE=InnoDB DEFAULT CHARSET={$CHARSET_DEFAULT} COLLATE={$COLLATE_TEXT};


-- ************************************** `auth_password`
CREATE TABLE IF NOT EXISTS `{$NAMESPACE}`.`auth_password` (
  `id`           INT(10) unsigned NOT NULL AUTO_INCREMENT,
  `sid`          VARBINARY(64) NOT NULL,
  `objectSID`    VARBINARY(64) NOT NULL,
  `passwordType` VARBINARY(64) NOT NULL,
  `passwordHash` VARBINARY(128) NOT NULL,
  `isRevoked`    TINYINT NOT NULL,
  `dateCreated`  INT(10) unsigned NOT NULL,
  `dateModified` INT(10) unsigned NOT NULL,
  `passwordSalt` VARCHAR(64) NOT NULL,

  PRIMARY KEY (`id`),
  UNIQUE KEY `key_sid` (`sid`),
  KEY `key_role` (`objectSID`,`passwordType`)
) ENGINE=InnoDB DEFAULT CHARSET={$CHARSET_DEFAULT} COLLATE={$COLLATE_TEXT};


-- ************************************** `auth_passwordtransaction`
CREATE TABLE IF NOT EXISTS `{$NAMESPACE}`.`auth_passwordtransaction` (
  `id`              INT(10) unsigned NOT NULL AUTO_INCREMENT,
  `sid`             VARBINARY(64) NOT NULL,
  `objectSID`       VARBINARY(64) NOT NULL,
  `authorSID`       VARBINARY(64) NOT NULL,
  `viewPolicy`      VARBINARY(64) NOT NULL,
  `editPolicy`      VARBINARY(64) NOT NULL,
  `transactionType` VARCHAR(32) NOT NULL,
  `oldValue`        LONGTEXT COLLATE {$COLLATE_TEXT} NOT NULL,
  `newValue`        LONGTEXT COLLATE {$COLLATE_TEXT} NOT NULL,
  `contentSource`   LONGTEXT COLLATE {$COLLATE_TEXT} NOT NULL,
  `metadata`        LONGTEXT COLLATE {$COLLATE_TEXT} NOT NULL,
  `dateCreated`     INT(10) unsigned NOT NULL,
  `dateModified`    INT(10) unsigned NOT NULL,

  PRIMARY KEY (`id`),
  UNIQUE KEY `key_sid` (`sid`),
  KEY `key_object` (`objectSID`)
) ENGINE=InnoDB DEFAULT CHARSET={$CHARSET_DEFAULT} COLLATE={$COLLATE_TEXT};

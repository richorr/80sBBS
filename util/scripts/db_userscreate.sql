
 create table if not exists _users (    
 	_partition_id bigint unsigned not null,
 	_key_id       bigint unsigned not null,
 	_created_dt   int unsigned not null,
 	_updated_dt   int unsigned not null,
 	_version      bigint unsigned not null,
 	_is_deleted   char(1) not null default 'N',
 	_compression  char(1) not null default 'F',
 	_value        blob not null,    
 	PRIMARY KEY(_key_id)
 	) 
 	ENGINE=InnoDB ROW_FORMAT=DYNAMIC CHARACTER SET utf8;
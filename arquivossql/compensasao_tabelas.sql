create database compensasao;
use compensasao;

create table empresas (
	idEmpresa int not null primary key,
    nmEmpresa varchar(100) not null,
    setorIndustria varchar(100)not null
);

create table localizacoes (
	idLoc int not null primary key,
    nmPais varchar(100) not null,
    nmCidade varchar(100) not null
);

create table empregos (
	idEmprego int not null primary key,
    nmEmprego varchar(100) not null,
    nivelExp varchar(50) not null,
    salarioDol decimal(10,2) not null,
    idEmpresa int,
    idLoc int,
    foreign key (idEmpresa)
    references empresas(idEmpresa),
    foreign key (idLoc)
    references localizacoes (idLoc)
);

create table habilidades (
	idHabilidade int not null primary key,
    nmHabilidade varchar(100) not null
);

create table empregoHabilidade (
	id int not null primary key,
    idEmprego int,
    idHabilidade int,
    foreign key (idEmprego)
    references empregos (idEmprego),
    foreign key (idHabilidade)
    references habilidades (idHabilidade)
);

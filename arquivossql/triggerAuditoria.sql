use compensasao;
drop table auditoria;
create table auditoria (
	idAud int auto_increment primary key,
    tabelaAlvo varchar(100),
    tipoOp varchar (10),
    datahora datetime,
    registro text
);

drop trigger tr_inserir;
delimiter //
create trigger tr_inserir
after insert on empregos
for each row
begin
	insert into auditoria (tabelaAlvo, tipoOp, datahora, registro)
    values ('empregos', 'insert', now(),
		concat(
        'id: ', new.idEmprego, 
        ', Nome: ', new.nmEmprego,
        ', Nível: ',  new.nivelExp,
        ', Salário: $', new.salarioDol,
        ', Id-Empresa: ', new.idEmpresa,
        ', Id-Localização: ', new.idLoc
        )
	);
end //
delimiter ;

select * from auditoria;

show triggers like 'empregos';
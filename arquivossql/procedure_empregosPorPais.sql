delimiter //
create procedure empregosPorPais (in nome_pais varchar(100))
begin
	select e.nmEmprego, e.nivelExp, e.salarioDol, emp.nmEmpresa, loc.nmPais
    from empregos e
    join empresas emp on e.idEmpresa = emp.idEmpresa
    join localizacoes loc on e.idLoc = loc.idLoc
    where loc.nmPais = nome_pais;
end //
delimiter ;

call empregosPorPais('United States');
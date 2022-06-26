create table contacto (
		codigo bigserial,
		nombre varchar(30),
		apellidos varchar(30),
		email varchar(30),
		telefono numeric(12),
		comentarios varchar(300),
		primary key (codigo)
);

create table login(
			logId bigserial,
			email varchar(30),
			passwrd varchar(30),
			primary key (logId)
			);
			
create table tienda(
			prodId bigserial,
			filtroTipo varchar(30),
			filtroStock numeric(30),
			primary key (prodId)
			);

create table registro (
		codigo bigserial,
		nombre varchar(30),
		apellidos varchar(30),
		rut numeric(10),
		dv numeric(1),
		email varchar(30),
		telefono numeric(12),
		primary key (codigo)
);
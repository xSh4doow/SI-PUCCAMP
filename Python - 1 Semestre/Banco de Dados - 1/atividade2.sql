#1
CREATE TABLE ENGS(
	id int auto_increment,
    nome varchar(30) not null,
    sexo enum ('M','F'),
    cpf bigint not null,
    salario double not null,
    fone int(10),
    primary key(id)
    );

INSERT INTO ENGS VALUES 
(1,'RICARDO','M',13789993315,1563.00,1932446784),
(2,'CLARA','F',12222646585,10675.75,1732446784),
(3,'RODRIGO','M',16789663215,3531.97, NULL),
(4,'FELIPE','M',12033335687,4765.90,1232446784),
(5,'LUISA','F',11789777214,7900.30,1933336784),
(6,'LAURA','F',13389647815,30090.50,1932550099),
(7,'FABIO','M',10313456778,4500.00, NULL),
(8,'HELENA','F',10789643215,4500.00,1522367532),
(9,'LUIZA','F',15786643335,35799.20,1232446787),
(10,'PAULO','M',10333643518,2300.00, NULL),
(11,'PEDRO','M',10375898854,2300.00,1932555567),
(12,'LUIZA','F',13456789643,2300.00,1532445361),
(13,'MIGUEL','M',13627890643,5000.00,1932748896),
(14,'JULIA','F',14446439210,6000.00,1932114509),
(15,'RENATO','M',10733211556,3000.00,1932433455),
(16,'CLARA','F',10988375542,5900.00,1932546678),
(17,'JULIANO','M',10222111215,4500.00,1932546678);


#2
UPDATE ENGS SET salario = 3000.50 WHERE salario < 2500 and sexo = 'M' or nome = 'Renato';

#3-4-5
UPDATE ENGS SET nome = 'Pedro', salario = '35000', sexo = 'M' WHERE nome = 'Juliano';

#6
UPDATE ENGS SET salario = 40000.50 WHERE (salario > 30000 and salario<36000) or nome = 'Julia';

#7
UPDATE ENGS SET fone = 1999871717 WHERE nome = 'Paulo';

#8
DELETE FROM ENGS WHERE salario < 2000 and sexo = 'M';

#9
DELETE FROM ENGS WHERE fone is NULL;

#10
DELETE FROM ENGS WHERE nome = 'Paulo';

#11
SELECT * FROM ENGS;

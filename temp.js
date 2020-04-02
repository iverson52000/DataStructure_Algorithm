select distinct nme, city from tblPerson
order by city

select columnList from leftTable
join rightTable
on leftTable.id = rightTable.id

create proc spGetEmployees
	as 
	begin
		select * from tblPerson
	end

select orderID, quantity,
case 
	when quantity > 30 then 'bigger > 30'
end as quantityText
from orderDetail
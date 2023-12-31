
    
    

select
    id as unique_field,
    count(*) as n_records

from massive_hotel.gold.customer_data
where id is not null
group by id
having count(*) > 1



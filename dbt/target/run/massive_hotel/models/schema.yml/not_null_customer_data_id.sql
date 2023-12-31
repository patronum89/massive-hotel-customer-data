select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select id
from massive_hotel.gold.customer_data
where id is null



      
    ) dbt_internal_test
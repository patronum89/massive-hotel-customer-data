select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select email
from massive_hotel.gold.customer_data
where email is null



      
    ) dbt_internal_test
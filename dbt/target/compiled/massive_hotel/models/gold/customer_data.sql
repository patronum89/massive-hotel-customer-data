



    select *
    from massive_hotel.silver.staging_customer_data
    qualify
        row_number() over (
            partition by 
  --  Takes an input list and generates a concat() statement with each argument in the list safe_casted to a string and wrapped in an ifnull()
  concat(
            id
            
        )

            order by 
  --  Takes an input list and generates a concat() statement with each argument in the list safe_casted to a string and wrapped in an ifnull()
  concat(
            updated_at
            
        )

        ) = 1



/*
    Welcome to your first dbt model!
    Did you know that you can also configure models directly within SQL files?
    This will override configurations stated in dbt_project.yml

    Try changing "table" to "view" below
*/

{{ config(materialized='table') }}

    -- Example transformation model
with raw_data as (

    select * from {{ ref('cheMed') }}
    union all
    select * from {{ ref('Doctorset') }}
    union all
    select * from {{ ref('EAHCI') }}
    union all
    select * from {{ ref('lobelia4cosmetics') }}
    union all
    select * from {{ ref('yetenaweg') }}

)

select 
    signature,
    channel_id,
    channel_name,
    msg_id,
    message,
    date	
from raw_data


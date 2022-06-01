# Write your MySQL query statement below
select i.invoice_id,
       c.customer_name,
       i.price,
       count(distinct t.contact_name) as contacts_cnt,
       sum(case when contact_name in (select distinct customer_name from Customers) then 1 else 0 end) as trusted_contacts_cnt
from Invoices as i
join Customers as c on c.customer_id = i.user_id
left join Contacts as t on c.customer_id = t.user_id
group by i.invoice_id
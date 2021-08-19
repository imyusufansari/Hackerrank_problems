/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
select E.company_code, C.founder, count(distinct lead_manager_code), count(distinct senior_manager_code), 
count(distinct manager_code), count(distinct employee_code) from Employee E inner join Company C 
on E.company_code = C.company_code group by E.company_code, C.founder order by E.company_code;

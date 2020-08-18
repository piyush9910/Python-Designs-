from covid import Covid

covid=Covid()
india=covid.get_status_by_country_name('India')
for i in india.items():
    print(i)
import info_parse
import info_db
import os
import collections

#init******************************************
f_name = ''
f = ''
#output*****************************************


#html API*****************************************
def html_writecol(list) :
    global f
    
    time = 'Time'
    f.write("data.addColumn('string', '%s')\n" % time)
    
    for colx, value  in enumerate(list):
        f.write("data.addColumn('number', '%s')\n" % value)
        
def composeColumns() :        
    ### display items row
    allItemList = info_db.getAllItemList()
     
    html_writecol(allItemList)    
    

def html_writerow(list) :
    global f
    
    f.write("[")
    for colx, value  in enumerate(list):
        if (colx == 0) :
            f.write("'%s', " % value)
        else :
            f.write("%s, " % value)

    f.write("],\n")
    
def composeRows() :
    ### display items row
    allItemList = info_db.getAllItemList()
    print allItemList
    
    ### display items array with time    
    sorted_items = collections.OrderedDict(sorted(info_db.Items_array.items()))
    for rowx, value in enumerate(sorted_items.items()) :
        #print '-------------------------------------------------------'
        #print time
        #print value

        #csv write time + items with empty
        #print info_db.composeOneLine(time, value)
        html_writerow(info_db.composeOneLine(value[0], value[1], allItemList))
        
def display_html(menu_name) :
    
    global f
    f_name = "%s.html" % menu_name
    f=open(f_name, 'w+')
    
    f.write("""
<html>
  <head>
    <script type="text/javascript"
          src="https://www.google.com/jsapi?autoload={
            'modules':[{
              'name':'visualization',
              'version':'1',
              'packages':['corechart']
            }]
          }"></script>

    <script type="text/javascript">
      google.setOnLoadCallback(drawChart);

      function drawChart() {
        var data = new google.visualization.DataTable();
""")
        #compose Columns
    composeColumns()

    f.write("""
        data.addRows([
    """)
        #compose Rows
    composeRows()

    f.write("""
        ]);
    
        var options = {
            hAxis: {
              title: 'Time'
            },
            vAxis: {
              title: 'Memory'
            },
            colors: ['#a52714', '#097138']
        };

        var chart = new google.visualization.LineChart(document.getElementById('curve_chart'));

        chart.draw(data, options);
      }
    </script>
  </head>
  <body>
    <div id="curve_chart" style="width: 1500px; height: 1500px"></div>
  </body>
</html>
    """)
    f.close()
    
def display_All(menu_list, input_file, output_file) :
    #global input_file
    
    for idx, value in enumerate(input_file) :
        print input_file[idx]
        if (os.path.isfile(input_file[idx]) == True) :            
            info_parse.init_parse(idx+1)
            info_parse.parse(input_file[idx])
            display_html(menu_list[idx])
        else:
            pass        
        
print 'END========================================'




        
    

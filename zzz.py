if request.method == 'POST':
        # Fetch form data
        cardDetails = request.form
        name = cardDetails['name']
        number = cardDetails['number']
        month = cardDetails['month']
        year = cardDetails['year']
        cvv = cardDetails['cvv']
        #password = userDetails['Password']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO  card(name, cardnum, month, year, cvv) VALUES(%s, %s, %s, %s, %s)",(name, number, month, year, cvv))
        mysql.connection.commit()
        cur.close()
        return redirect('/package.html')

















<script type="text/javascript">
function checkFluency()
{
  var checkbox = document.getElementById('fluency');
  if (checkbox.checked != true)
  {
    alert("you need to be fluent in English to apply for the job");
  }
}
</script>
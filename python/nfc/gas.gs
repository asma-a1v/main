function doGet(e) {
  //doPost(e)にするとformからのpostデータを書き込むことが出来る
  //応用すれば、スプレッドシートをRestAPIもどきにしたり、フォームのDBにしたり、いろいろ出来ると思う
  //別名で使いたい場合の例
  //var name = e.parameter.p1;
  //var mail = e.parameter.p2;

  //JSONオブジェクト格納用の入れ物
  var rowData = {};  

  if (e.parameter == undefined) {

      //パラメータ不良の場合はundefinedで返す
      var getvalue = "undefined"

      //エラーはJSONで返すつもりなので
      rowData.value = getvalue;
      var result = JSON.stringify(rowData);
      return ContentService.createTextOutput(result);

  }else{

      //書込先スプレッドシートのIDを入力
      var id = '1EXWJBlIAb1KNcety4oEGi--XFTMYQ_5SH-Cl6Z8q9gI';

      //スプレッドシート名指定 "シート1"
      var sheet = SpreadsheetApp.openById(id).getSheetByName("シート1");

      //Getした値を配列にする
      //https://xxxxxxxxx/exec?p1=AAA&p2=BBB&p3=CCC&p4=DDDD
      //こんな感じなのを以下のように配列してappendRowで追記する
      var array = [ e.parameter.p1 , e.parameter.p2 , e.parameter.p3];

      //シートに配列を書き込み
      sheet.appendRow(array);

      //書き込み終わったらOKを返す
      var getvalue = "ok"

      //エラーはJSONで返すつもりなので
      rowData.value = getvalue;
      var result = JSON.stringify(rowData);
      return ContentService.createTextOutput(result);

  }
}
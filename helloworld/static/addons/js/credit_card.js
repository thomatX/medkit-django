function loadBanks() {
    var names = [
        "BBVA",
        "Banco del Desarrollo",
        "Banco Chile/Edwards",
        "Banco Internacional",
        "Banco Estado",
        "Banco ScotiaBank",
        "Banco BCI",
        "Banco de Brasil S.A",
        "Corpbanca",
        "Banco BICE",
        "Banco HSBC Bank",
        "Banco Santander",
        "Banco Itau",
        "Banco Security",
        "Banco Falabella",
        "Banco Ripley",
        "RaboBank",
        "Banco Consorcio",
        "Banco Paris",
        "Coopeuch"
        ]

        var $list = $("#cardBank");
        for(var i=0; i<names.length; i++) {
            $list.append('<option value="'+i+'">' + names[i] + '</option>');
        }
}
$(document).ready(function () {
    loadBanks();
});



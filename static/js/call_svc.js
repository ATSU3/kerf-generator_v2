function call_kerf_check() {
    var json = { 'stw': 0, 'inc': 0, 'gap': 0, 'lp': 0, 'tbone': 0 };

    json.stw = Number(par_form.form_st.value);
    json.inc = Number(par_form.form_inc.value);
    json.gap = Number(par_form.form_gap.value);
    json.lp = Number(par_form.form_lp.value);
    json.tbone = Number(par_form.form_tbone.value);

    var json_txt = JSON.stringify(json);
    var req = new XMLHttpRequest;

    req.onload = function () {
        var res = req.responseText;
        const blob = new Blob([res], { type: 'image/svg+xml' });
        var blobUrl = window.URL.createObjectURL(blob);
        var download = document.getElementById('download');
        var img = document.getElementById('result');

        download.href = blobUrl;
        img.src = blobUrl;
    };

    req.onerror = function () {
        alert('エラー');
    }

    req.open('post', '/kerf_check', true);
    req.setRequestHeader('Content-Type', 'application/json');
    req.send(json_txt);
}
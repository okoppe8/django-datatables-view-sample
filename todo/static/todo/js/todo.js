/*
 * 定数定義（疑似列挙型）
 */

// データの配列と列の順番の対応
let Columns = {
    "id": 0,
    "status": 1,
    "title": 2,
    "detail": 3,
    "created_at": 4,
    "updated_at": 5,
}

// タスクのステータス
let Status = {
    "waiting": "0", // 未着手
    "working": "1", // 対応中
    "done": "2"     // 完了
}

/*
 * jQuery
 */

$(document).ready(function () {

    /*
     * DataTablesの設定
     */

    let table = $('#datatable').DataTable({

        // Ajax設定
        processing: true,
        serverSide: true,
        ajax: "./api/datatables",

        // ビューの設定
        dom: "tp",
        pageLength: 10,
        order: [Columns.updated_at, "desc"],   // 更新時間が新しい順


        language: {
            "sInfoEmpty": "データ無し",
            "sZeroRecords": "データはありません。",
            "oPaginate": {
                "sFirst": "<<",
                "sPrevious": "<",
                "sNext": ">",
                "sLast": ">>"
            },
        },

        // 列の設定
        columns: [

            // 「className: "none",」と定義した列は詳細行に表示される

            {
                // 1列目 id (非表示)
                title: "&nbsp;",
                visible: false,
            },
            {
                // 2列目 status (非表示)
                title: "状況",
                visible: false,
            },
            {
                // 3列目 title
                title: "タイトル",
                orderable: false,
            },
            {
                // 4列目 detail
                title: "詳細",
                className: "none",
            },
            {
                // 5列目 created_at
                title: "登録時間",
                className: "none",
                render: function (data) {
                    return moment(data).format('YYYY/MM/DD HH:mm:ss')
                }
            },
            {
                // 6列目 updated_at
                title: "更新時間",
                className: "none",
                render: function (data) {
                    return moment(data).format('YYYY/MM/DD HH:mm:ss')
                }
            },
            {
                // 7列目 ボタン表示
                title: "操作",
                className: "none",
                data: 0,

                // データ操作欄の表示
                render: function (data, type, row) {

                    // ステータスで判定
                    let status = row[Columns.status];

                    let back_disabled, forward_disabled, forward_label;

                    switch (status) {
                        case Status.waiting:
                            back_disabled = "disabled"
                            forward_disabled = "";
                            forward_label = "着手";
                            break;
                        case Status.working:
                            back_disabled = ""
                            forward_disabled = "";
                            forward_label = "完了";
                            break;
                        case Status.done:
                            back_disabled = ""
                            forward_disabled = "disabled";
                            forward_label = "完了";
                            break;
                    }

                    // HTMLの出力
                    let content =
                        '<span class="btn-container" data-id="' + row[Columns.id] + '">'
                        + '<button class="btn btn-outline-dark mr-3 popup">編集</button>'
                        + '<div class="btn-group">'
                        + '<button value="-1" class="btn btn-outline-dark operation"' + back_disabled + '>戻す</button>'
                        + '<button value="1" class="btn btn-outline-dark operation"' + forward_disabled + ' >'
                        + forward_label + '</button>'
                        + '</div></span>';

                    return content;
                },

            },
        ],
    });

    /*
     * 入力フォームの表示処理
     */

    // 追加もしくは編集ボタンクリックでフォーム表示
    $(document).on("click", "button.popup", function () {

        // フォームの初期化
        $("input#id_id").val("");
        $("form#form")[0].reset();
        $("form#form").find("input")
            .removeClass("is-invalid")
            .nextAll("span.invalid-feedback").remove();

        // 呼び出したボタンの属性を見て追加か編集か判定する
        let id = ($(this).parents(".btn-container").attr("data-id"));

        if (!id) {
            // 追加モード
            $('h5.modal-title').text("新規")
            $('button#delete').hide();
        } else {
            // 編集モード
            $('h5.modal-title').text("編集")
            $('button#delete').show();

            // サーバからデータを取得する
            $.ajax({
                type: "get",
                url: "api/tasks/" + id,
                dataType: "json"
            })
                .done(function (data) {
                    $.each(data, function (key, value) {
                        $("form#form").find("#id_" + key).val(value)
                    })
                })
                .fail(function (jqXHR, textStatus, errorThrown) {
                    alert("サーバーエラー！");
                    console.log(jqXHR);
                })
        }
        $('#modal').modal("show");
    })

    /*
     * 保存ボタン（追加・編集共通）の処理
     */

    $("button#save").on("click", function () {

        $("form#form").addClass("disabled");

        let id, url, type

        // 追加か編集（idの有無で判定）によってエンドポイントを変える。
        id = $('#id_id').val();
        if (!id) {
            // 追加モード
            url = "api/tasks/"
            type = "post"
        } else {
            // 編集モード
            url = "api/tasks/" + id + "/"
            type = "put"
        }

        // サーバへの送信処理
        $.ajax({
            type: type,
            url: url,
            data: $("form#form").serialize(),
        }).done(function (data) {
            $("#modal").modal("hide");
            table.draw();
        }).fail(function (jqXHR, textStatus, errorThrown) {

            if (jqXHR.status == 400) {

                // 最初に既存のエラー表示を解除する。
                $("form#form").find("input")
                    .removeClass("is-invalid")
                    .nextAll("span.invalid-feedback").remove();

                // 入力フォーム内にエラーを反映させる。
                $.each(jqXHR.responseJSON,
                    function (key, value) {
                        $("form#form").find("#id_" + key)
                            .addClass("is-invalid")
                            .after('<span class="invalid-feedback"><strong>' + value + "</strong></span>")
                    })
            } else {
                alert("サーバーエラー！");
                console.log(jqXHR);
            }
        }).always(function () {
            $('form#form').removeClass("disabled");
        })
    });

    /*
     * 削除ボタンの処理
     */
    $('button#delete').on("click", function () {
        let id;

        id = $('#id_id').val();
        $.ajax({
            type: "patch",
            url: "api/tasks/" + id + "/",
            data: {id: id, is_deleted: true},
        }).done(function (data) {
            table.draw();
        }).fail(function (jqXHR, textStatus, errorThrown) {
            alert("サーバーエラー！");
            console.log(jqXHR);
        }).always(function () {
            $('#modal').modal("hide");
        })
    })

    /*
     * 戻す・着手（完了）ボタンの処理
     */

    $(document).on("click", "button.operation", function () {

        let id, status, opetation

        id = ($(this).parents('.btn-container').attr("data-id"));
        status = $('input[name="status"]:checked').val();
        opetation = $(this).val()

        // サーバへの送信処理
        $.ajax({
            type: "patch",
            url: "api/tasks/" + id + "/",
            data: {id: id, status: parseInt(status) + parseInt(opetation)},
        }).done(function (data) {
            table.draw();
        }).fail(function (jqXHR, textStatus, errorThrown) {
            alert("サーバーエラー！");
            console.log(jqXHR);
        })
    })


    /*
     * ビューの切り替えボタンの動作
     */

    $('input[type="radio"]').on("change", function () {
        // ボタンのvalueに設定したステータス値で検索する
        status = $('input[name="status"]:checked').val();
        table.column(Columns.status).search(status).draw();
    }).change();

    /*
     * 入力フォーム上でリターンキーを押下したときの送信を防ぐ
     */

    $('form#form').on("submit", function (e) {
        e.preventDefault();
    })
});
/**
 * Created by LittleFrog on 2020/4/19.
 */
$(function () {

    var data = {}
    var info
    //页面加载完请求课程数据
    $.ajax({
        type: "GET",
        url: "/teacher/get_course_data",
        success: function (msg) {
            info = JSON.parse(msg)
            for (var i = 0; i < info.length; i++) {
                if (info[i].className in data)
                    data[info[i].className].push(info[i].courseName)
                else
                    data[info[i].className] = [info[i].courseName]
            }
            //添加下拉框选项
            var first = true
            for (var key in data) {
                $("#class").append($("<option>" + key + "</option>"))
                if (first) {
                    for (var i in data[key]) {
                        $("#course").append($("<option>" + data[key][i] + "</option>"))
                    }
                    first = false
                }
            }
            //联动
            $("#class").change(function () {
                var className = $("#class option:selected").text()
                for (var key in data) {
                    if (key == className) {
                        $("#course").empty()
                        for (var i in data[key]) {
                            $("#course").append($("<option>" + data[key][i] + "</option>"))
                        }
                    }
                }
            })
        },
        error: function (xhr) {
            alert("请求失败：" + xhr.status)
        }
    })

    //查询
    $("#search").click(function () {
        var className = $("#class option:selected").text()
        var courseName = $("#course option:selected").text()
        var info2 = {}
        for(var i=0; i<info.length; i++){
            if(className == info[i].className)
                info2["classNumber"] = info[i].classNumber
            if(courseName == info[i].courseName)
                info2["courseNumber"] = info[i].courseNumber
        }
        $.ajax({
            type: "POST",
            url: "/teacher/get_value_data",
            data: {info: JSON.stringify(info2)},
            success: function (msg) {
                console.log(ok);
            },
            error: function (xhr) {
                alert("请求失败：" + xhr.status)
            }
        })
    })


    //导入课程评价值excel
    $("#import").click(function () {
        //创建文件读取对象
        var reader = new FileReader()
        //获取用户选择的文件
        var file = $("#upload")[0].files[0]
        //读取文件
        reader.readAsBinaryString(file)
        //文件成功读取完成后时
        reader.onload = function (e) {
            var data = e.target.result;
            var workbook = XLSX.read(data, {type: 'binary'});
            var worksheet = workbook.Sheets.Sheet1
            //记录学生评价值的对象
            var info = {
                courseName: '概率论与数理统计', //$("#course option:selected").text()
                points: [],
                value: []
            }
            for (var key in worksheet) {
                // v读取单元格的原始值 w读取格式化后的内容
                if (key[0] != '!') {
                    if (key[1] == '1' && key[0] != 'A') { //取出表头的指标点编号
                        info.points.push(worksheet[key].w)
                    }
                    else if (key[1] != '1') { //表体内容
                        if (key[0] == 'A') //记录学号
                            info.value.push({
                                //记录学生在各个指标点上评价值的对象
                                studentNumber: worksheet[key].w,
                                point: []
                            })
                        else //记录评价值
                            info.value[info.value.length - 1].point.push(worksheet[key].v)
                    }
                }
            }
            $.ajax({
                type: "POST",
                url: "/teacher/import_course_data",
                data: {info: JSON.stringify(info)},
                success: function (msg) {
                    $("#ok").click()
                },
                error: function (xhr) {
                    alert("请求失败：" + xhr.status)
                }
            })
        }
    })
})
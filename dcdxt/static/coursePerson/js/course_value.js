/**
 * Created by LittleFrog on 2020/4/19.
 */
$(function () {

    //注销
    $("#exit").click(function () {
        $.ajax({
            type: 'GET',
            url: "/exit",
            success:function () {
                window.location = '/login'
            },
            error: function (xhr) {
                alert("请求失败：" + xhr.status)
            }
        })
    })

    //请求课程数据
    var data = {}
    var info
    $.ajax({
        type: "GET",
        url: "/coursePerson/course_examine",
        success: function (msg) {
            info = JSON.parse(msg)
            console.log(info);
            for (var i = 0; i < info.length; i++) {
                data[info[i]['className']] = info[i]['course_list']
            }
            //添加下拉框选项
            var first = true
            for (var key in data) {
                $("#class").append($("<option>" + key + "</option>"))
                if (first) {
                    for (var i in data[key]) {
                        $("#course").append($("<option>" + data[key][i]['courseName'] + "</option>"))
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
                            $("#course").append($("<option>" + data[key][i]['courseName'] + "</option>"))
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
        for (var i = 0; i < info.length; i++) {
            if (className == info[i].className) {
                info2["classNumber"] = info[i].classNumber
                for (var j = 0; j < info[i]['course_list'].length; j++) {
                    if (courseName == info[i]['course_list'][j].courseName)
                        info2["courseNumber"] = info[i]['course_list'][j].courseNumber
                }
            }
        }
        $.ajax({
            type: "POST",
            url: "/coursePerson/get_examine",
            data: {info: JSON.stringify(info2)},
            success: function (msg) {
                var msg = JSON.parse(msg)
                console.log(msg);
                //饼状图
                var myChart = echarts.init(document.getElementById('picture'), 'light');
                myChart.setOption({
                    series: [
                        {
                            name: '课程评价值',
                            type: 'pie',    // 设置图表类型为饼图
                            radius: '48%',  // 饼图的半径，外半径为可视区尺寸（容器高宽中较小一项）的 55% 长度。
                            // roseType: 'angle', //把饼图显示成南丁格尔图
                            data: [  // 数据数组，name 为数据项名称，value 为数据项值
                                {value: msg["level_1"], name: '达成度>=0.9'},
                                {value: msg["level_2"], name: '达成度>=0.8'},
                                {value: msg["level_3"], name: '达成度>=0.65'},
                                {value: msg["level_4"], name: '达成度<0.65'}
                            ]
                        }
                    ]
                })
                //统计信息
                $("#box").html("<h4>最高评价值：" + msg['max_value'] + "</h4><h4>最低评价值：" + msg['min_value'] + "</h4><h4>平均评价值：" + msg['avg_value'].toFixed(2) + "</h4><br>")
                //审核状态
                if (msg['status'] == 0) {
                    $("#box").append($('<button class="btn btn-default" style="margin-right: 20px" id="pass">审核通过</button>'))
                    $("#box").append($('<button class="btn btn-default" id="notpass">审核不通过</button>'))
                    //审核通过
                    $("#pass").click(function () {
                        var className = $("#class option:selected").text()
                        var courseName = $("#course option:selected").text()
                        var info3 = {}
                        for (var i = 0; i < info.length; i++) {
                            if (className == info[i].className) {
                                info3["classNumber"] = info[i].classNumber
                                for (var j = 0; j < info[i]['course_list'].length; j++) {
                                    if (courseName == info[i]['course_list'][j].courseName)
                                        info3["courseNumber"] = info[i]['course_list'][j].courseNumber
                                }
                            }
                        }
                        info3['status'] = 1
                        console.log(info3);
                        $.ajax({
                            type: "POST",
                            url: "/coursePerson/examine",
                            data: {info: JSON.stringify(info3)},
                            success: function (msg) {
                                $("#box").append($('<h3 style="color: #4cae4c;">审核通过</h3>'))
                                $("#box button").remove()
                            },
                            error: function (xhr) {
                                alert("请求失败：" + xhr.status)
                            }
                        })
                    })
                    //审核不通过
                    $("#notpass").click(function () {
                        var className = $("#class option:selected").text()
                        var courseName = $("#course option:selected").text()
                        var info3 = {}
                        for (var i = 0; i < info.length; i++) {
                            if (className == info[i].className) {
                                info3["classNumber"] = info[i].classNumber
                                for (var j = 0; j < info[i]['course_list'].length; j++) {
                                    if (courseName == info[i]['course_list'][j].courseName)
                                        info3["courseNumber"] = info[i]['course_list'][j].courseNumber
                                }
                            }
                        }
                        info3['status'] = 2
                        console.log(info3);
                        $.ajax({
                            type: "POST",
                            url: "/coursePerson/examine",
                            data: {info: JSON.stringify(info3)},
                            success: function (msg) {
                                $("#box").append($('<h3 style="color: orangered">审核不通过</h3>'))
                                $("#box button").remove()
                            },
                            error: function (xhr) {
                                alert("请求失败：" + xhr.status)
                            }
                        })
                    })
                }
                else if (msg['status'] == 1) {
                    $("#box").append($('<h3 style="color: #4cae4c;">审核通过</h3>'))

                }
                else if (msg['status'] == 2) {
                    $("#box").append($('<h3 style="color: orangered">审核不通过</h3>'))
                }
            },
            error: function (xhr) {
                alert("请求失败：" + xhr.status)
            }
        })
    })
})
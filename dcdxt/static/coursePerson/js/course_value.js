/**
 * Created by LittleFrog on 2020/4/19.
 */
$(function () {

    //注销
    $("#exit").click(function () {
        $.ajax({
            type: 'GET',
            url: "/exit",
            success: function () {
                window.location = "/login/"
            },
            error: function (xhr) {
                alert("请求失败：" + xhr.status)
            }
        })
        window.location = 'login.html'
    })

    //请求课程数据
    var data = {}
    var info
    $.ajax({
        type: "GET",
        url: "/coursePerson/course_examine",
        success: function (msg) {
            info = JSON.parse(msg)
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
                //为每个指标点生成统计信息
                for (var i = 0; i < msg['data'].length; i++) {
                    //饼状图
                    var picture = $('<div class="picture"></div>')
                    var box = $('<div class="box"></div>')
                    $("#pictures").append(picture).append(box)
                    var myChart = echarts.init($(".picture").eq(i)[0], 'light');
                    myChart.setOption({
                        title: {
                            text: "指标点 " + msg['data'][i]["point"],
                            subtext: $("#class option:selected").text() + $("#course option:selected").text() + "在指标点" + msg['data'][i]["point"] + "上的课程评价值分布情况",
                            x: 'center'
                        },
                        series: [
                            {
                                name: '课程评价值',
                                type: 'pie',    // 设置图表类型为饼图
                                radius: '48%',  // 饼图的半径，外半径为可视区尺寸（容器高宽中较小一项）的 55% 长度。
                                // roseType: 'angle', //把饼图显示成南丁格尔图
                                data: [  // 数据数组，name 为数据项名称，value 为数据项值
                                    {value: msg['data'][i]["level_1"], name: '达成度>=0.9'},
                                    {value: msg['data'][i]["level_2"], name: '达成度>=0.8'},
                                    {value: msg['data'][i]["level_3"], name: '达成度>=0.65'},
                                    {value: msg['data'][i]["level_4"], name: '达成度<0.65'}
                                ]
                            }
                        ]
                    })
                    //统计信息
                    $(".box").eq(i).html("<h4>最高评价值：" + msg['data'][i]['max_value'] + "</h4><h4>最低评价值：" + msg['data'][i]['min_value'] + "</h4><h4>平均评价值：" + msg['data'][i]['avg_value'].toFixed(2) + "</h4><br>")
                    $(".box").eq(i).css({
                        top: 300 + i * 440,
                        left: 580
                    })
                }
                //审核状态
                if (msg['status'] == 0) {
                    $("#evaluate").append($('<button class="btn pull-right btn-danger" id="notpass">审核不通过</button>'))
                    $("#evaluate").append($('<button class="btn pull-right btn-success" style="margin-right: 20px" id="pass">审核通过</button>'))
                    //审核通过
                    $("#pass").click(function () {
                        var className = $("#class option:selected").text()
                        var courseName = $("#course option:selected").text()
                        var info3 = {}
                        for (var j = 0; j < info.length; j++) {
                            if (className == info[j].className) {
                                info3["classNumber"] = info[j].classNumber
                                for (var k = 0; k < info[j]['course_list'].length; k++) {
                                    if (courseName == info[j]['course_list'][k].courseName)
                                        info3["courseNumber"] = info[j]['course_list'][k].courseNumber
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
                                $("#evaluate").children('button').remove()
                                $("#evaluate").append($('<button class="disabled btn btn-success pull-right">已审核通过</button>'))
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
                        for (var j = 0; j < info.length; j++) {
                            if (className == info[j].className) {
                                info3["classNumber"] = info[j].classNumber
                                for (var k = 0; k < info[j]['course_list'].length; k++) {
                                    if (courseName == info[j]['course_list'][k].courseName)
                                        info3["courseNumber"] = info[j]['course_list'][k].courseNumber
                                }
                            }
                        }
                        info3['status'] = 2
                        $.ajax({
                            type: "POST",
                            url: "/coursePerson/examine",
                            data: {info: JSON.stringify(info3)},
                            success: function (msg) {
                                $("#evaluate").children('button').remove()
                                $("#evaluate").append($('<button class="disabled btn btn-danger pull-right">已审核不通过</button>'))
                            },
                            error: function (xhr) {
                                alert("请求失败：" + xhr.status)
                            }
                        })

                        //反馈意见弹框
                        $("#no").click()
                        var info4 = {}
                        info4["classNumber"] = info3["classNumber"]
                        info4["courseNumber"] = info3["courseNumber"]
                        $("#feedback").click(function () {
                            info4["feedback"] = $("#comment").val()
                            // console.log(JSON.stringify(info4));
                            $.ajax({
                                type: "POST",
                                url: "/coursePerson/feedback",
                                data: {info: JSON.stringify(info4)},
                                success: function (msg) {
                                },
                                error: function (xhr) {
                                    alert("请求失败：" + xhr.status)
                                }
                            })
                        })
                    })
                }
                else if (msg['status'] == 1) {
                    $("#evaluate").append($('<button class="disabled btn btn-success pull-right">已审核通过</button>'))
                }
                else if (msg['status'] == 2) {
                    $("#evaluate").append($('<button class="disabled btn btn-danger pull-right">已审核不通过</button>'))
                }
            },
            error: function (xhr) {
                $("#ok").click()
            }
        })
    })
})
/**
 * Created by LittleFrog on 2020/4/19.
 */
$(function () {

    //请求课程数据
    $.ajax({
        type: "GET",
        url: "/coursePerson/course_examine",
        success: function (msg) {
            console.log(msg);
        },
        error: function (xhr) {
            alert("请求失败：" + xhr.status)
        }
    })

    //查询
    $("#search").click(function () {
        var info = {}
        $.ajax({
            type: "POST",
            url: "/coursePerson/get_examine",
            data: {info: info},
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
                $("#box").html("<h4>最高评价值"+msg['max_value']+"</h4><br><h4>最低评价值"+msg['min_value']+"</h4><br><h4>平均评价值"+msg['avg_value']+"</h4>")
            },
            error: function (xhr) {
                alert("请求失败：" + xhr.status)
            }
        })
    })
})
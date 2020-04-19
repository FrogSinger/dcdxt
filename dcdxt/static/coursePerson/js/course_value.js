/**
 * Created by LittleFrog on 2020/4/19.
 */
$(function () {

    //饼状图
    var myChart = echarts.init(document.getElementById('picture'),'light');
    myChart.setOption({
        series : [
            {
                name: '访问来源',
                type: 'pie',    // 设置图表类型为饼图
                radius: '55%',  // 饼图的半径，外半径为可视区尺寸（容器高宽中较小一项）的 55% 长度。
                // roseType: 'angle', //把饼图显示成南丁格尔图
                data:[  // 数据数组，name 为数据项名称，value 为数据项值
                    {value:235, name:'达成度>=0.9'},
                    {value:274, name:'达成度>=0.8'},
                    {value:310, name:'达成度>=0.65'},
                    {value:335, name:'达成度<0.65'}
                ]
            }
        ]
    })
})
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

    //下载导入模板
    $("#download").click(function () {
         $.ajax({
            type:"POST",
            url:"/majorPerson/download_template",
            error:function (xhr) {
                alert("下载失败：" + xhr.status)
            }
        })
    })

    //指标点跟着毕业要求级联变动
    $("#req").change(function () {
        switch ($(this)[0].selectedIndex) {
            case 0:
                $("#point").empty().append($("<option>指标点1-1</option>")).append($("<option>指标点1-2</option>")).append($("<option>指标点1-3</option>"))
                break
            case 1:
                $("#point").empty().append($("<option>指标点2-1</option>")).append($("<option>指标点2-2</option>")).append($("<option>指标点2-3</option>"))
                break
            case 2:
                $("#point").empty().append($("<option>指标点3-1</option>")).append($("<option>指标点3-2</option>")).append($("<option>指标点3-3</option>")).append($("<option>指标点3-4</option>")).append($("<option>指标点3-5</option>"))
                break
            case 3:
                $("#point").empty().append($("<option>指标点4-1</option>")).append($("<option>指标点4-2</option>")).append($("<option>指标点4-3</option>"))
                break
            case 4:
                $("#point").empty().append($("<option>指标点5-1</option>")).append($("<option>指标点5-2</option>")).append($("<option>指标点5-3</option>"))
                break
            case 5:
                $("#point").empty().append($("<option>指标点6-1</option>")).append($("<option>指标点6-2</option>"))
                break
            case 6:
                $("#point").empty().append($("<option>指标点7-1</option>")).append($("<option>指标点7-2</option>"))
                break
            case 7:
                $("#point").empty().append($("<option>指标点8-1</option>")).append($("<option>指标点8-2</option>"))
                break
            case 8:
                $("#point").empty().append($("<option>指标点9-1</option>")).append($("<option>指标点9-2</option>"))
                break
            case 9:
                $("#point").empty().append($("<option>指标点11-1</option>")).append($("<option>指标点11-2</option>"))
                break
            case 10:
                $("#point").empty().append($("<option>指标点12-1</option>")).append($("<option>指标点12-2</option>")).append($("<option>指标点12-3</option>"))
                break
            case 11:
                $("#point").empty().append($("<option>指标点5-1</option>")).append($("<option>指标点5-2</option>")).append($("<option>指标点5-3</option>"))
                break
        }
    })

    //搜索
    $("#search").click(function () {
        var point = $("#point option:selected").text().substring(3)
        $.ajax({
            type:"POST",
            url:"/majorPerson/get_matrix",
            data:{point:point},
            success:function (msg) {
                //将后端返回的数据转成json格式
                msg = JSON.parse(msg)
                //清空表格内容 添加数据
                $("#table").empty()
                for(var i=0; i<msg.length; i++){
                    $("#table").append($("<tr><td>"+(i+1)+"</td><td>"+msg[i]["courseNumber"]+"</td><td>"+
                        msg[i]["courseName"]+"</td><td>"+msg[i]["weight"]+"</td></tr>"))
                }

            },
            error:function (xhr) {
                alert("请求失败：" + xhr.status)
            }
        })
    })

    //导入支撑课程体系excel
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
            //记录毕业要求
            var req = []
            //记录指标点
            var point = []
            //记录课程
            var course = []
            //记录指标点和课程之间的联系
            var point_course = []
            //遍历excel表单元格
            for(var key in worksheet) {
                // v读取单元格的原始值 w读取格式化后的内容
                if(key[0] != '!'){
                    //提取毕业要求
                    if(key[0] == 'A' && key in worksheet){
                        req.push({
                            number: worksheet[key].w
                        })
                    }
                    if(key[0] == 'B' && key in worksheet){
                        req[req.length-1].content = worksheet[key].v
                    }
                    //提取指标点
                    if(key[0] == 'C' && key in worksheet){
                        point.push({
                            number: worksheet[key].v,
                            GraduationReq: req[req.length-1].number
                        })
                    }
                    if(key[0] == 'D' && key in worksheet){
                        point[point.length-1].content = worksheet[key].v
                    }
                    //提取课程
                    if(key[0] == 'E'){
                        course.push({
                            courseNumber: worksheet[key].w
                        })
                    }
                    if(key[0] == 'F'){
                        course[course.length-1].name = worksheet[key].v
                    }
                    //提取指标点和课程之间的联系
                    if(key[0] == 'E'){
                        point_course.push({
                            course: worksheet[key].v,
                            point: point[point.length-1].number
                        })
                    }
                    if(key[0] == 'G' && key in worksheet){
                        point_course[point_course.length-1].weight = worksheet[key].v
                    }
                }
            }
            req.shift()
            point.shift()
            course.shift()
            point_course.shift()
            var course_norepeat = []
            var flag = {}
            for(var i=1; i<course.length; i++){
                if(!(course[i].courseNumber in flag)){
                    course_norepeat.push(course[i])
                    flag[course[i].courseNumber] = true
                }
            }
            var info = {
                    req:req,
                    point:point,
                    course:course_norepeat,
                    point_course_matrix:point_course
                }
            $.ajax({
                type:"POST",
                url:"/majorPerson/import_interface",
                data: {info:JSON.stringify(info)},
                success:function (msg) {
                    $("#ok").click()
                },
                error:function (xhr) {
                    alert("请求失败：" + xhr.status)
                }
            })
        }
    })

    //下载导入模板
    $("#download").click(function () {
        window.location = "/majorPerson/download_template"
    })
})
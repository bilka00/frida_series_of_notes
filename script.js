var message = Memory.allocUtf8String("It`s work");

Interceptor.attach(Module.findExportByName("user32.dll", "MessageBoxA"), {
    onEnter: function(args)
    {
        console.log("Execute MessageBoxA")
        console.log(args[1].readUtf8String());
        args[1] = message;
    },
    onLeave: function(retval)
    {
    }
});
// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package io.muehlbachler.pulumi.proxmoxve;

import com.pulumi.core.Output;
import com.pulumi.core.TypeShape;
import com.pulumi.deployment.Deployment;
import com.pulumi.deployment.InvokeOptions;
import com.pulumi.resources.InvokeArgs;
import io.muehlbachler.pulumi.proxmoxve.Utilities;
import io.muehlbachler.pulumi.proxmoxve.inputs.GetDNSArgs;
import io.muehlbachler.pulumi.proxmoxve.inputs.GetDNSPlainArgs;
import io.muehlbachler.pulumi.proxmoxve.inputs.GetHostsArgs;
import io.muehlbachler.pulumi.proxmoxve.inputs.GetHostsPlainArgs;
import io.muehlbachler.pulumi.proxmoxve.inputs.GetTimeArgs;
import io.muehlbachler.pulumi.proxmoxve.inputs.GetTimePlainArgs;
import io.muehlbachler.pulumi.proxmoxve.outputs.GetDNSResult;
import io.muehlbachler.pulumi.proxmoxve.outputs.GetHostsResult;
import io.muehlbachler.pulumi.proxmoxve.outputs.GetTimeResult;
import io.muehlbachler.pulumi.proxmoxve.outputs.GetVersionResult;
import java.util.concurrent.CompletableFuture;

public final class ProxmoxveFunctions {
    public static Output<GetDNSResult> getDNS(GetDNSArgs args) {
        return getDNS(args, InvokeOptions.Empty);
    }
    public static CompletableFuture<GetDNSResult> getDNSPlain(GetDNSPlainArgs args) {
        return getDNSPlain(args, InvokeOptions.Empty);
    }
    public static Output<GetDNSResult> getDNS(GetDNSArgs args, InvokeOptions options) {
        return Deployment.getInstance().invoke("proxmoxve:index/getDNS:getDNS", TypeShape.of(GetDNSResult.class), args, Utilities.withVersion(options));
    }
    public static CompletableFuture<GetDNSResult> getDNSPlain(GetDNSPlainArgs args, InvokeOptions options) {
        return Deployment.getInstance().invokeAsync("proxmoxve:index/getDNS:getDNS", TypeShape.of(GetDNSResult.class), args, Utilities.withVersion(options));
    }
    public static Output<GetHostsResult> getHosts(GetHostsArgs args) {
        return getHosts(args, InvokeOptions.Empty);
    }
    public static CompletableFuture<GetHostsResult> getHostsPlain(GetHostsPlainArgs args) {
        return getHostsPlain(args, InvokeOptions.Empty);
    }
    public static Output<GetHostsResult> getHosts(GetHostsArgs args, InvokeOptions options) {
        return Deployment.getInstance().invoke("proxmoxve:index/getHosts:getHosts", TypeShape.of(GetHostsResult.class), args, Utilities.withVersion(options));
    }
    public static CompletableFuture<GetHostsResult> getHostsPlain(GetHostsPlainArgs args, InvokeOptions options) {
        return Deployment.getInstance().invokeAsync("proxmoxve:index/getHosts:getHosts", TypeShape.of(GetHostsResult.class), args, Utilities.withVersion(options));
    }
    public static Output<GetTimeResult> getTime(GetTimeArgs args) {
        return getTime(args, InvokeOptions.Empty);
    }
    public static CompletableFuture<GetTimeResult> getTimePlain(GetTimePlainArgs args) {
        return getTimePlain(args, InvokeOptions.Empty);
    }
    public static Output<GetTimeResult> getTime(GetTimeArgs args, InvokeOptions options) {
        return Deployment.getInstance().invoke("proxmoxve:index/getTime:getTime", TypeShape.of(GetTimeResult.class), args, Utilities.withVersion(options));
    }
    public static CompletableFuture<GetTimeResult> getTimePlain(GetTimePlainArgs args, InvokeOptions options) {
        return Deployment.getInstance().invokeAsync("proxmoxve:index/getTime:getTime", TypeShape.of(GetTimeResult.class), args, Utilities.withVersion(options));
    }
    public static Output<GetVersionResult> getVersion() {
        return getVersion(InvokeArgs.Empty, InvokeOptions.Empty);
    }
    public static CompletableFuture<GetVersionResult> getVersionPlain() {
        return getVersionPlain(InvokeArgs.Empty, InvokeOptions.Empty);
    }
    public static Output<GetVersionResult> getVersion(InvokeArgs args) {
        return getVersion(args, InvokeOptions.Empty);
    }
    public static CompletableFuture<GetVersionResult> getVersionPlain(InvokeArgs args) {
        return getVersionPlain(args, InvokeOptions.Empty);
    }
    public static Output<GetVersionResult> getVersion(InvokeArgs args, InvokeOptions options) {
        return Deployment.getInstance().invoke("proxmoxve:index/getVersion:getVersion", TypeShape.of(GetVersionResult.class), args, Utilities.withVersion(options));
    }
    public static CompletableFuture<GetVersionResult> getVersionPlain(InvokeArgs args, InvokeOptions options) {
        return Deployment.getInstance().invokeAsync("proxmoxve:index/getVersion:getVersion", TypeShape.of(GetVersionResult.class), args, Utilities.withVersion(options));
    }
}
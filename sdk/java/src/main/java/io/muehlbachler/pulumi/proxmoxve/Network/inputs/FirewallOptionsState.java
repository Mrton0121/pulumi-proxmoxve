// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package io.muehlbachler.pulumi.proxmoxve.Network.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.Boolean;
import java.lang.Integer;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class FirewallOptionsState extends com.pulumi.resources.ResourceArgs {

    public static final FirewallOptionsState Empty = new FirewallOptionsState();

    /**
     * The ID of the container to manage the firewall for.
     * 
     */
    @Import(name="containerId")
    private @Nullable Output<Integer> containerId;

    /**
     * @return The ID of the container to manage the firewall for.
     * 
     */
    public Optional<Output<Integer>> containerId() {
        return Optional.ofNullable(this.containerId);
    }

    /**
     * Enable DHCP
     * 
     */
    @Import(name="dhcp")
    private @Nullable Output<Boolean> dhcp;

    /**
     * @return Enable DHCP
     * 
     */
    public Optional<Output<Boolean>> dhcp() {
        return Optional.ofNullable(this.dhcp);
    }

    /**
     * Enable or disable the firewall
     * 
     */
    @Import(name="enabled")
    private @Nullable Output<Boolean> enabled;

    /**
     * @return Enable or disable the firewall
     * 
     */
    public Optional<Output<Boolean>> enabled() {
        return Optional.ofNullable(this.enabled);
    }

    /**
     * Default policy for incoming traffic
     * 
     */
    @Import(name="inputPolicy")
    private @Nullable Output<String> inputPolicy;

    /**
     * @return Default policy for incoming traffic
     * 
     */
    public Optional<Output<String>> inputPolicy() {
        return Optional.ofNullable(this.inputPolicy);
    }

    /**
     * Enable default IP filters. This is equivalent to adding an empty ipfilter-net&lt;id&gt; ipset for every interface. Such ipsets
     * implicitly contain sane default restrictions such as restricting IPv6 link local addresses to the one derived from the
     * interface&#39;s MAC address. For containers the configured IP addresses will be implicitly added.
     * 
     */
    @Import(name="ipfilter")
    private @Nullable Output<Boolean> ipfilter;

    /**
     * @return Enable default IP filters. This is equivalent to adding an empty ipfilter-net&lt;id&gt; ipset for every interface. Such ipsets
     * implicitly contain sane default restrictions such as restricting IPv6 link local addresses to the one derived from the
     * interface&#39;s MAC address. For containers the configured IP addresses will be implicitly added.
     * 
     */
    public Optional<Output<Boolean>> ipfilter() {
        return Optional.ofNullable(this.ipfilter);
    }

    /**
     * Log level for incoming traffic.
     * 
     */
    @Import(name="logLevelIn")
    private @Nullable Output<String> logLevelIn;

    /**
     * @return Log level for incoming traffic.
     * 
     */
    public Optional<Output<String>> logLevelIn() {
        return Optional.ofNullable(this.logLevelIn);
    }

    /**
     * Log level for outgoing traffic.
     * 
     */
    @Import(name="logLevelOut")
    private @Nullable Output<String> logLevelOut;

    /**
     * @return Log level for outgoing traffic.
     * 
     */
    public Optional<Output<String>> logLevelOut() {
        return Optional.ofNullable(this.logLevelOut);
    }

    /**
     * Enable MAC address filtering
     * 
     */
    @Import(name="macfilter")
    private @Nullable Output<Boolean> macfilter;

    /**
     * @return Enable MAC address filtering
     * 
     */
    public Optional<Output<Boolean>> macfilter() {
        return Optional.ofNullable(this.macfilter);
    }

    /**
     * Enable NDP (Neighbor Discovery Protocol)
     * 
     */
    @Import(name="ndp")
    private @Nullable Output<Boolean> ndp;

    /**
     * @return Enable NDP (Neighbor Discovery Protocol)
     * 
     */
    public Optional<Output<Boolean>> ndp() {
        return Optional.ofNullable(this.ndp);
    }

    /**
     * The name of the node.
     * 
     */
    @Import(name="nodeName")
    private @Nullable Output<String> nodeName;

    /**
     * @return The name of the node.
     * 
     */
    public Optional<Output<String>> nodeName() {
        return Optional.ofNullable(this.nodeName);
    }

    /**
     * Default policy for outgoing traffic
     * 
     */
    @Import(name="outputPolicy")
    private @Nullable Output<String> outputPolicy;

    /**
     * @return Default policy for outgoing traffic
     * 
     */
    public Optional<Output<String>> outputPolicy() {
        return Optional.ofNullable(this.outputPolicy);
    }

    /**
     * Allow sending Router Advertisement
     * 
     */
    @Import(name="radv")
    private @Nullable Output<Boolean> radv;

    /**
     * @return Allow sending Router Advertisement
     * 
     */
    public Optional<Output<Boolean>> radv() {
        return Optional.ofNullable(this.radv);
    }

    /**
     * The ID of the VM to manage the firewall for.
     * 
     */
    @Import(name="vmId")
    private @Nullable Output<Integer> vmId;

    /**
     * @return The ID of the VM to manage the firewall for.
     * 
     */
    public Optional<Output<Integer>> vmId() {
        return Optional.ofNullable(this.vmId);
    }

    private FirewallOptionsState() {}

    private FirewallOptionsState(FirewallOptionsState $) {
        this.containerId = $.containerId;
        this.dhcp = $.dhcp;
        this.enabled = $.enabled;
        this.inputPolicy = $.inputPolicy;
        this.ipfilter = $.ipfilter;
        this.logLevelIn = $.logLevelIn;
        this.logLevelOut = $.logLevelOut;
        this.macfilter = $.macfilter;
        this.ndp = $.ndp;
        this.nodeName = $.nodeName;
        this.outputPolicy = $.outputPolicy;
        this.radv = $.radv;
        this.vmId = $.vmId;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(FirewallOptionsState defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private FirewallOptionsState $;

        public Builder() {
            $ = new FirewallOptionsState();
        }

        public Builder(FirewallOptionsState defaults) {
            $ = new FirewallOptionsState(Objects.requireNonNull(defaults));
        }

        /**
         * @param containerId The ID of the container to manage the firewall for.
         * 
         * @return builder
         * 
         */
        public Builder containerId(@Nullable Output<Integer> containerId) {
            $.containerId = containerId;
            return this;
        }

        /**
         * @param containerId The ID of the container to manage the firewall for.
         * 
         * @return builder
         * 
         */
        public Builder containerId(Integer containerId) {
            return containerId(Output.of(containerId));
        }

        /**
         * @param dhcp Enable DHCP
         * 
         * @return builder
         * 
         */
        public Builder dhcp(@Nullable Output<Boolean> dhcp) {
            $.dhcp = dhcp;
            return this;
        }

        /**
         * @param dhcp Enable DHCP
         * 
         * @return builder
         * 
         */
        public Builder dhcp(Boolean dhcp) {
            return dhcp(Output.of(dhcp));
        }

        /**
         * @param enabled Enable or disable the firewall
         * 
         * @return builder
         * 
         */
        public Builder enabled(@Nullable Output<Boolean> enabled) {
            $.enabled = enabled;
            return this;
        }

        /**
         * @param enabled Enable or disable the firewall
         * 
         * @return builder
         * 
         */
        public Builder enabled(Boolean enabled) {
            return enabled(Output.of(enabled));
        }

        /**
         * @param inputPolicy Default policy for incoming traffic
         * 
         * @return builder
         * 
         */
        public Builder inputPolicy(@Nullable Output<String> inputPolicy) {
            $.inputPolicy = inputPolicy;
            return this;
        }

        /**
         * @param inputPolicy Default policy for incoming traffic
         * 
         * @return builder
         * 
         */
        public Builder inputPolicy(String inputPolicy) {
            return inputPolicy(Output.of(inputPolicy));
        }

        /**
         * @param ipfilter Enable default IP filters. This is equivalent to adding an empty ipfilter-net&lt;id&gt; ipset for every interface. Such ipsets
         * implicitly contain sane default restrictions such as restricting IPv6 link local addresses to the one derived from the
         * interface&#39;s MAC address. For containers the configured IP addresses will be implicitly added.
         * 
         * @return builder
         * 
         */
        public Builder ipfilter(@Nullable Output<Boolean> ipfilter) {
            $.ipfilter = ipfilter;
            return this;
        }

        /**
         * @param ipfilter Enable default IP filters. This is equivalent to adding an empty ipfilter-net&lt;id&gt; ipset for every interface. Such ipsets
         * implicitly contain sane default restrictions such as restricting IPv6 link local addresses to the one derived from the
         * interface&#39;s MAC address. For containers the configured IP addresses will be implicitly added.
         * 
         * @return builder
         * 
         */
        public Builder ipfilter(Boolean ipfilter) {
            return ipfilter(Output.of(ipfilter));
        }

        /**
         * @param logLevelIn Log level for incoming traffic.
         * 
         * @return builder
         * 
         */
        public Builder logLevelIn(@Nullable Output<String> logLevelIn) {
            $.logLevelIn = logLevelIn;
            return this;
        }

        /**
         * @param logLevelIn Log level for incoming traffic.
         * 
         * @return builder
         * 
         */
        public Builder logLevelIn(String logLevelIn) {
            return logLevelIn(Output.of(logLevelIn));
        }

        /**
         * @param logLevelOut Log level for outgoing traffic.
         * 
         * @return builder
         * 
         */
        public Builder logLevelOut(@Nullable Output<String> logLevelOut) {
            $.logLevelOut = logLevelOut;
            return this;
        }

        /**
         * @param logLevelOut Log level for outgoing traffic.
         * 
         * @return builder
         * 
         */
        public Builder logLevelOut(String logLevelOut) {
            return logLevelOut(Output.of(logLevelOut));
        }

        /**
         * @param macfilter Enable MAC address filtering
         * 
         * @return builder
         * 
         */
        public Builder macfilter(@Nullable Output<Boolean> macfilter) {
            $.macfilter = macfilter;
            return this;
        }

        /**
         * @param macfilter Enable MAC address filtering
         * 
         * @return builder
         * 
         */
        public Builder macfilter(Boolean macfilter) {
            return macfilter(Output.of(macfilter));
        }

        /**
         * @param ndp Enable NDP (Neighbor Discovery Protocol)
         * 
         * @return builder
         * 
         */
        public Builder ndp(@Nullable Output<Boolean> ndp) {
            $.ndp = ndp;
            return this;
        }

        /**
         * @param ndp Enable NDP (Neighbor Discovery Protocol)
         * 
         * @return builder
         * 
         */
        public Builder ndp(Boolean ndp) {
            return ndp(Output.of(ndp));
        }

        /**
         * @param nodeName The name of the node.
         * 
         * @return builder
         * 
         */
        public Builder nodeName(@Nullable Output<String> nodeName) {
            $.nodeName = nodeName;
            return this;
        }

        /**
         * @param nodeName The name of the node.
         * 
         * @return builder
         * 
         */
        public Builder nodeName(String nodeName) {
            return nodeName(Output.of(nodeName));
        }

        /**
         * @param outputPolicy Default policy for outgoing traffic
         * 
         * @return builder
         * 
         */
        public Builder outputPolicy(@Nullable Output<String> outputPolicy) {
            $.outputPolicy = outputPolicy;
            return this;
        }

        /**
         * @param outputPolicy Default policy for outgoing traffic
         * 
         * @return builder
         * 
         */
        public Builder outputPolicy(String outputPolicy) {
            return outputPolicy(Output.of(outputPolicy));
        }

        /**
         * @param radv Allow sending Router Advertisement
         * 
         * @return builder
         * 
         */
        public Builder radv(@Nullable Output<Boolean> radv) {
            $.radv = radv;
            return this;
        }

        /**
         * @param radv Allow sending Router Advertisement
         * 
         * @return builder
         * 
         */
        public Builder radv(Boolean radv) {
            return radv(Output.of(radv));
        }

        /**
         * @param vmId The ID of the VM to manage the firewall for.
         * 
         * @return builder
         * 
         */
        public Builder vmId(@Nullable Output<Integer> vmId) {
            $.vmId = vmId;
            return this;
        }

        /**
         * @param vmId The ID of the VM to manage the firewall for.
         * 
         * @return builder
         * 
         */
        public Builder vmId(Integer vmId) {
            return vmId(Output.of(vmId));
        }

        public FirewallOptionsState build() {
            return $;
        }
    }

}